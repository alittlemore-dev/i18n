from collections.abc import Iterator
from importlib import reload

import pytest
from httpx import Response
from litestar import Litestar
from litestar.testing import TestClient

from entrypoints.litestar.api import routers
from entrypoints.litestar.api.i18n import endpoints
from entrypoints.litestar.initializers import main as initializer
from main import create_app


def create_app_with_current_settings(monkeypatch: pytest.MonkeyPatch) -> Litestar:
    # Static route decorators read configuration at import time, as on process startup.
    reload(endpoints)
    reload(routers)
    monkeypatch.setattr(initializer, "api_router", routers.api_router)
    return create_app()


class I18nTestApi:
    def __init__(self, client: TestClient, prefix: str) -> None:
        self.client = client
        self.prefix = prefix

    def get_i18n_languages(self) -> Response:
        return self.client.get("/api/i18n/languages")

    def get_i18n_bundle(self, *, bundle: str, language: str) -> Response:
        return self.client.get(f"{self.prefix}/bundles/{bundle}/{language}")


class ApiTestCase:
    bundle_prefix = "/api/i18n"
    api: I18nTestApi

    @pytest.fixture(autouse=True)
    def api_client(self) -> Iterator[None]:
        with TestClient(create_app()) as client:
            self.api = I18nTestApi(client, self.bundle_prefix)
            yield
