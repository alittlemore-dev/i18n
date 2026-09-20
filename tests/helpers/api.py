from collections.abc import Iterator

import pytest
from httpx import Response
from litestar.testing import TestClient

from main import create_app


class I18nTestApi:
    def __init__(self, client: TestClient, prefix: str) -> None:
        self.client = client
        self.prefix = prefix

    def get_i18n_languages(self) -> Response:
        return self.client.get("/api/i18n/languages")

    def get_i18n_bundle(self, *, language: str) -> Response:
        return self.client.get(f"{self.prefix}/bundles/{language}")


class ApiTestCase:
    bundle_prefix = "/api/i18n"
    api: I18nTestApi

    @pytest.fixture(autouse=True)
    def api_client(self) -> Iterator[None]:
        with TestClient(create_app()) as client:
            self.api = I18nTestApi(client, self.bundle_prefix)
            yield
