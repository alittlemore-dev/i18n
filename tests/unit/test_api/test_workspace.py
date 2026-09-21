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
        assert body["messages"]["workspaceDashboard.tools.summary"] == "Cache"
        assert "dashboard.tools.summary" not in body["messages"]

    def test_rejects_unknown_bundle_language(self) -> None:
        response = self.api.get_i18n_bundle(bundle="personal-workspace", language="de")

        assert response.status_code == codes.BAD_REQUEST, response.content
