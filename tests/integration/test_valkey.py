import uuid

import pytest
from litestar import get
from litestar.testing import AsyncTestClient
from valkey.asyncio import Valkey

from core.i18n.catalogs import CATALOGS
from core.i18n.enums import CatalogEnum, LanguageEnum
from infra.config.constants import constants
from infra.config.settings import settings
from main import create_app
from tests.helpers.api import create_app_with_current_settings


async def test_real_valkey_readiness_and_response_cache(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(settings.app, "use_cache", True)
    path = f"/test-cache-{uuid.uuid4().hex}"
    calls = []

    @get(path, cache=30)
    async def cached() -> dict[str, int]:
        calls.append(1)
        return {"calls": len(calls)}

    app = create_app()
    app.register(cached)
    async with AsyncTestClient(app) as client:
        response = await client.get("/api/i18n/healthcheck/ready")
        assert response.status_code == 200
        assert response.content == b""
        first = await client.get(path)
        second = await client.get(path)
        assert first.json() == second.json() == {"calls": 1}
        assert len(calls) == 1
        async with Valkey.from_url(settings.valkey.url) as valkey:
            keys = [
                key
                async for key in valkey.scan_iter(match=f"{constants.valkey.namespace}:*{path}*")
            ]
            assert len(keys) == 1
            assert await valkey.ttl(keys[0]) > 0
            await valkey.delete(*keys)


async def test_cache_disabled_executes_each_request(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(settings.app, "use_cache", False)
    calls = []

    @get("/uncached")
    async def uncached() -> int:
        calls.append(1)
        return len(calls)

    app = create_app()
    app.register(uncached)
    async with AsyncTestClient(app) as client:
        assert (await client.get("/uncached")).json() == 1
        assert (await client.get("/uncached")).json() == 2


async def test_catalog_responses_use_versioned_isolated_valkey_cache(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    namespace = f"I18N_TEST_{uuid.uuid4().hex}"
    monkeypatch.setattr(settings.app, "use_cache", True)
    monkeypatch.setattr(constants.valkey, "namespace", namespace)
    paths = [
        f"/api/i18n{prefix}/bundles/{language}"
        for prefix in ("", "/personal-workspace")
        for language in ("ru", "en")
    ]
    async with Valkey.from_url(settings.valkey.url) as valkey:
        try:
            async with AsyncTestClient(create_app_with_current_settings(monkeypatch)) as client:
                for path in paths:
                    first = await client.get(path)
                    second = await client.get(path)
                    assert first.status_code == 200
                    assert second.json() == first.json()
                assert (await client.get("/api/i18n/languages")).json()["defaultLanguage"] == "ru"
            original_keys = {key async for key in valkey.scan_iter(match=f"{namespace}:*")}
            assert len(original_keys) == 5
            for key in original_keys:
                assert 86_390 <= await valkey.ttl(key) <= 86_400

            changed = {
                catalog: {language: dict(bundle) for language, bundle in messages.items()}
                for catalog, messages in CATALOGS.items()
            }
            changed[CatalogEnum.WORKSPACE][LanguageEnum.EN]["app.siteName"] = "New workspace title"
            monkeypatch.setattr("core.i18n.service.CATALOGS", changed)
            monkeypatch.setattr("entrypoints.litestar.api.i18n.cache.CATALOGS", changed)
            async with AsyncTestClient(create_app_with_current_settings(monkeypatch)) as client:
                response = await client.get("/api/i18n/personal-workspace/bundles/en")
                assert response.json()["messages"]["app.siteName"] == "New workspace title"
            new_keys = {key async for key in valkey.scan_iter(match=f"{namespace}:*")}
            assert len(new_keys - original_keys) == 1
        finally:
            keys = [key async for key in valkey.scan_iter(match=f"{namespace}:*")]
            if keys:
                await valkey.delete(*keys)
