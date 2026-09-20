from dishka import Provider, Scope, provide

from core.i18n.service import I18nService
from infra.config.settings import settings


class I18nProvider(Provider):
    @provide(scope=Scope.APP)
    def provide_i18n(self) -> I18nService:
        return I18nService(default_language=settings.i18n.default_language)
