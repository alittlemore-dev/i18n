from tests.helpers.api import ApiTestCase


class TestHealthcheckCatalog(ApiTestCase):
    def test_healthcheck_catalog_available_in_both_languages(self) -> None:
        russian = self.api.get_i18n_bundle(bundle="admin-panel", language="ru").json()["messages"]
        english = self.api.get_i18n_bundle(bundle="admin-panel", language="en").json()["messages"]
        expected = {
            "dashboard.healthcheck.title",
            "dashboard.healthcheck.system.backups",
            "dashboard.healthcheck.lastSuccess",
            "dashboard.healthcheck.restoreNotVerified",
            "dashboard.healthcheck.unavailable",
            *(
                f"dashboard.healthcheck.status.{status}"
                for status in (
                    "healthy",
                    "initializing",
                    "degraded",
                    "stale",
                    "failed",
                    "unavailable",
                )
            ),
            *(
                f"dashboard.healthcheck.role.{role}"
                for role in ("latest", "weekly_current", "weekly_previous")
            ),
        }
        for messages in (russian, english):
            assert expected <= messages.keys()
            assert all(messages[key].strip() for key in expected)
        assert {key for key in russian if key.startswith("dashboard.healthcheck.")} == {
            key for key in english if key.startswith("dashboard.healthcheck.")
        }
