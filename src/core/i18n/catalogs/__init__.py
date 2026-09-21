from collections.abc import Mapping

from core.i18n.catalogs import (
    account,
    admin_panel,
    articles,
    competency_matrix,
    how_this_site_is_built,
    personal_workspace,
    shared,
    sitemap,
    updates,
)
from core.i18n.enums import BundleEnum, LanguageEnum

BUNDLES: Mapping[BundleEnum, Mapping[LanguageEnum, Mapping[str, str]]] = {
    BundleEnum.SHARED: shared.MESSAGES,
    BundleEnum.HOW_THIS_SITE_IS_BUILT: how_this_site_is_built.MESSAGES,
    BundleEnum.ARTICLES: articles.MESSAGES,
    BundleEnum.COMPETENCY_MATRIX: competency_matrix.MESSAGES,
    BundleEnum.UPDATES: updates.MESSAGES,
    BundleEnum.SITEMAP: sitemap.MESSAGES,
    BundleEnum.ACCOUNT: account.MESSAGES,
    BundleEnum.ADMIN_PANEL: admin_panel.MESSAGES,
    BundleEnum.PERSONAL_WORKSPACE: personal_workspace.MESSAGES,
}
