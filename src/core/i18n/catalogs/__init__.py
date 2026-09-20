from collections.abc import Mapping

from core.i18n.catalogs import competency, workspace
from core.i18n.enums import CatalogEnum, LanguageEnum

CATALOGS: Mapping[CatalogEnum, Mapping[LanguageEnum, Mapping[str, str]]] = {
    CatalogEnum.COMPETENCY: competency.MESSAGES,
    CatalogEnum.WORKSPACE: workspace.MESSAGES,
}
