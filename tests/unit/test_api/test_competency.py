from string import Formatter

from httpx import codes

from tests.helpers.api import ApiTestCase

ACCOUNT_MESSAGE_KEYS = {
    "shell.account.profile",
    "shared.unsavedChanges.confirmDiscard",
    "account.title",
    "account.navigation",
    "account.profile.title",
    "account.profile.edit",
    "account.profile.fullName",
    "account.profile.firstName",
    "account.profile.lastName",
    "account.profile.middleName",
    "account.profile.gender",
    "account.profile.gender.male",
    "account.profile.gender.female",
    "account.profile.username",
    "account.profile.changeAvatar",
    "account.profile.removeAvatar",
    "account.profile.avatarAlt",
    "account.profile.loading",
    "account.profile.loadFailed",
    "account.profile.retry",
    "account.profile.saveSuccess",
    "account.profile.avatarSaveSuccess",
    "account.profile.saveFailed",
    "account.profile.avatarFailed",
    "account.profile.invalidAvatarType",
    "account.profile.avatarTooLarge",
}


class TestI18nApi(ApiTestCase):
    def test_account_messages_exist_and_match_across_languages(self) -> None:
        russian = {
            **self.api.get_i18n_bundle(bundle="shared", language="ru").json()["messages"],
            **self.api.get_i18n_bundle(bundle="account", language="ru").json()["messages"],
        }
        english = {
            **self.api.get_i18n_bundle(bundle="shared", language="en").json()["messages"],
            **self.api.get_i18n_bundle(bundle="account", language="en").json()["messages"],
        }

        assert russian.keys() >= ACCOUNT_MESSAGE_KEYS
        assert english.keys() >= ACCOUNT_MESSAGE_KEYS
        for key in ACCOUNT_MESSAGE_KEYS:
            assert self._placeholders(russian[key]) == self._placeholders(english[key])

        assert russian["shell.account.profile"] == "Профиль"
        assert english["shell.account.profile"] == "Profile"
        assert russian["shared.notSet"] == "Не задано"
        assert english["shared.notSet"] == "Not set"
        assert russian["shared.unsavedChanges.confirmDiscard"] == (
            "Есть несохранённые изменения. Если продолжить, они будут потеряны. Продолжить?"
        )
        assert english["shared.unsavedChanges.confirmDiscard"] == (
            "You have unsaved changes. If you continue, they will be lost. Continue?"
        )

    def test_list_languages(self) -> None:
        response = self.api.get_i18n_languages()

        assert response.status_code == codes.OK, response.content
        assert response.json() == {
            "defaultLanguage": "ru",
            "languages": [
                {"code": "ru", "label": "Русский"},
                {"code": "en", "label": "English"},
            ],
        }

    def test_get_russian_bundle(self) -> None:
        response = self.api.get_i18n_bundle(bundle="admin-panel", language="ru")

        assert response.status_code == codes.OK, response.content
        body = response.json()
        assert body["bundle"] == "admin-panel"
        assert body["language"] == "ru"
        assert body["messages"]["adminPanel.title"] == "Админ-панель"

    def test_shared_bundle_contains_global_account_feedback(self) -> None:
        shared = self.api.get_i18n_bundle(bundle="shared", language="en").json()["messages"]
        account = self.api.get_i18n_bundle(bundle="account", language="en").json()["messages"]

        required = {
            "account.settings.title",
            "account.settings.saved",
            "account.settings.saveFailed",
            "account.settings.applyFailed",
        }
        assert required <= shared.keys()
        assert required.isdisjoint(account.keys())

    def test_get_english_bundle(self) -> None:
        response = self.api.get_i18n_bundle(bundle="admin-panel", language="en")

        assert response.status_code == codes.OK, response.content
        body = response.json()
        assert body["bundle"] == "admin-panel"
        assert body["language"] == "en"
        assert body["messages"]["adminPanel.title"] == "Admin panel"

    def test_unknown_bundle_language_is_rejected(self) -> None:
        response = self.api.get_i18n_bundle(bundle="shared", language="de")

        assert response.status_code == codes.BAD_REQUEST

    def test_unknown_bundle_is_rejected(self) -> None:
        response = self.api.get_i18n_bundle(bundle="missing", language="en")

        assert response.status_code == codes.BAD_REQUEST

    def test_legacy_bundle_paths_are_removed(self) -> None:
        assert self.api.client.get("/api/i18n/bundles/en").status_code == codes.NOT_FOUND
        assert (
            self.api.client.get("/api/i18n/personal-workspace/bundles/en").status_code
            == codes.NOT_FOUND
        )

    @staticmethod
    def _placeholders(message: str) -> set[str]:
        return {name for _, name, _, _ in Formatter().parse(message) if name is not None}
