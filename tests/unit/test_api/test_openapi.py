from collections.abc import Iterator

import pytest
from litestar import Litestar
from litestar.testing import TestClient
from pydantic import TypeAdapter
from verbose_http_exceptions.exc.base import VerboseHTTPExceptionDict

from entrypoints.litestar.api.i18n.schemas import LanguagesResponseSchema
from main import create_app


@pytest.fixture
def app() -> Litestar:
    return create_app()


@pytest.fixture
def client(app: Litestar) -> Iterator[TestClient]:
    with TestClient(app) as test_client:
        yield test_client


def test_public_operations_describe_language_and_bundle_contract(app: Litestar) -> None:
    schema = app.openapi_schema.to_schema()
    paths = schema["paths"]
    assert set(paths) == {"/api/i18n/languages", "/api/i18n/bundles/{bundle}/{language}"}
    for path in paths.values():
        operation = path["get"]
        assert operation["summary"]
        assert operation["description"]
        assert not operation.get("security")
        assert "401" not in operation["responses"]
        assert "403" not in operation["responses"]
    parameters = paths["/api/i18n/bundles/{bundle}/{language}"]["get"]["parameters"]
    for parameter in parameters:
        assert parameter["required"] is True
        assert parameter["in"] == "path"
        assert parameter["description"]
        reference = parameter["schema"]["$ref"].rsplit("/", 1)[-1]
        assert schema["components"]["schemas"][reference]["examples"]


def test_success_examples_are_supported_by_the_current_catalog(
    app: Litestar,
    client: TestClient,
) -> None:
    schemas = app.openapi_schema.to_schema()["components"]["schemas"]
    response = client.get("/api/i18n/languages")
    assert response.status_code == 200
    LanguagesResponseSchema.model_validate(response.json())
    properties = schemas["LanguageResponseSchema"]["properties"]
    for language in response.json()["languages"]:
        assert language["label"] in properties["label"]["examples"]
    properties = schemas["I18nBundleResponseSchema"]["properties"]
    bundle_schema = schemas[properties["bundle"]["$ref"].rsplit("/", 1)[-1]]
    language_schema = schemas[properties["language"]["$ref"].rsplit("/", 1)[-1]]
    bundle = bundle_schema["examples"][0]
    language = language_schema["examples"][0]
    response = client.get(f"/api/i18n/bundles/{bundle}/{language}")
    assert response.status_code == 200
    for example in properties["messages"]["examples"]:
        for key, value in example.items():
            assert response.json()["messages"][key] == value


def test_error_responses_document_real_verbose_envelope(
    app: Litestar,
    client: TestClient,
) -> None:
    schema = app.openapi_schema.to_schema()
    paths = schema["paths"]
    operation = paths["/api/i18n/bundles/{bundle}/{language}"]["get"]
    assert "400" in operation["responses"]
    assert "422" not in operation["responses"]
    error_schema = schema["components"]["schemas"]["VerboseHTTPExceptionDict"]
    assert set(error_schema["required"]) == {"code", "type", "message", "location", "attr"}
    assert "nested_errors" in error_schema["properties"]
    adapter = TypeAdapter(VerboseHTTPExceptionDict)
    for path in paths.values():
        for status, response in path["get"]["responses"].items():
            if int(status) < 400:
                continue
            content = response["content"]["application/json"]
            assert content["schema"] == {"$ref": "#/components/schemas/VerboseHTTPExceptionDict"}
            for example in content["examples"].values():
                adapter.validate_python(example["value"])
    for url in ("/api/i18n/bundles/shared/de", "/api/i18n/bundles/unknown/de"):
        response = client.get(url)
        assert response.status_code == 400
        adapter.validate_python(response.json())
    assert len(response.json()["nested_errors"]) == 2
