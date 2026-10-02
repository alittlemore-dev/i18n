import pytest
from httpx import codes

from tests.helpers.api import ApiTestCase


class TestI18nApi(ApiTestCase):
    def test_lists_configured_languages(self) -> None:
        response = self.api.get_i18n_languages()

        assert response.status_code == codes.OK, response.content
        assert response.json() == {
            "defaultLanguage": "ru",
            "languages": [
                {"code": "ru", "label": "Русский"},
                {"code": "en", "label": "English"},
            ],
        }

    def test_returns_requested_language_bundle(self) -> None:
        response = self.api.get_i18n_bundle(bundle="personal-workspace", language="en")

        assert response.status_code == codes.OK, response.content
        body = response.json()
        assert body["bundle"] == "personal-workspace"
        assert body["language"] == "en"
        assert body["messages"]["workspace.title"] == "Workspace"
        assert body["messages"]["workspaceDashboard.calendar.title"] == "Calendar"
        assert "dashboard.tools.summary" not in body["messages"]

    @pytest.mark.parametrize("language", ["ru", "en"])
    def test_returns_workspace_cache_tools_in_admin_bundle(self, language: str) -> None:
        response = self.api.get_i18n_bundle(bundle="admin-panel", language=language)

        assert response.status_code == codes.OK, response.content
        messages = response.json()["messages"]
        assert "Personal Workspace" in messages["adminWorkspaceTools.cache.title"]
        for key in ("warm", "clear", "pollError", "warmSuccess"):
            assert messages[f"adminWorkspaceTools.cache.{key}"].strip()

    def test_rejects_unknown_bundle_language(self) -> None:
        response = self.api.get_i18n_bundle(bundle="personal-workspace", language="de")

        assert response.status_code == codes.BAD_REQUEST, response.content
