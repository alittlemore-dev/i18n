import uuid

import pytest
from litestar import get
from litestar.testing import AsyncTestClient
from valkey.asyncio import Valkey

from infra.config.constants import constants
from infra.config.settings import settings
from main import create_app


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
