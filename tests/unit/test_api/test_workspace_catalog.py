from core.i18n.catalogs import BUNDLES
from core.i18n.enums import BundleEnum, LanguageEnum


def get_i18n_messages(language: LanguageEnum) -> dict[str, str]:
    return {
        **BUNDLES[BundleEnum.SHARED][language],
        **BUNDLES[BundleEnum.PERSONAL_WORKSPACE][language],
    }


class TestI18nCatalog:
    def test_authentication_experience_copy_is_available_and_nonblank(self) -> None:
        required_keys = {
            "auth.login.title",
            "auth.login.subtitle",
            "auth.login.username",
            "auth.login.password",
            "auth.login.submit",
            "auth.login.submitting",
            "auth.login.invalidCredentials",
            "auth.login.rateLimited",
            "auth.login.forbidden",
            "auth.login.serviceError",
            "auth.login.validationError",
            "auth.sessionExpired.title",
            "auth.sessionExpired.message",
            "auth.logout",
            "auth.logout.submitting",
            "auth.logout.failed",
            "auth.currentUser",
        }

        for language in LanguageEnum:
            messages = get_i18n_messages(language=language)
            assert required_keys <= messages.keys()
            assert all(messages[key].strip() for key in required_keys)

    def test_supported_languages_have_identical_keys(self) -> None:
        russian_keys = set(get_i18n_messages(language=LanguageEnum.RU))
        english_keys = set(get_i18n_messages(language=LanguageEnum.EN))

        assert english_keys == russian_keys

    def test_publish_status_values_have_labels_in_every_language(self) -> None:
        required_keys = {
            "enum.publishStatus.Draft",
            "enum.publishStatus.Published",
        }
        for language in LanguageEnum:
            assert required_keys <= get_i18n_messages(language).keys()

    def test_retained_workspace_copy_is_localized_in_both_languages(self) -> None:
        required_keys = {
            "workspace.section.dashboard",
            "workspace.section.resumes",
            "workspace.section.tools",
            "workspace.section.knowledge",
            "workspace.section.people",
            "workspace.section.dates",
            "knowledgePeople.relationshipTypes.manage",
            "knowledgePeople.attachmentDownloadError",
            "knowledgeDates.attachmentDownloadError",
            "tools.cache.title",
            "resumeWorkspace.title",
        }

        for language in LanguageEnum:
            messages = get_i18n_messages(language=language)
            assert required_keys <= messages.keys()
            assert all(messages[key].strip() for key in required_keys)

    def test_markdown_editor_accessibility_copy_is_localized(self) -> None:
        russian = get_i18n_messages(language=LanguageEnum.RU)
        english = get_i18n_messages(language=LanguageEnum.EN)

        assert russian["markdownEditor.toolbar.aria"] == "Действия Markdown-редактора"
        assert english["markdownEditor.toolbar.aria"] == "Markdown editor actions"
        assert "Escape" in russian["markdownEditor.shortcuts.tabEscape"]
        assert "Tab" in english["markdownEditor.shortcuts.tabEscape"]
