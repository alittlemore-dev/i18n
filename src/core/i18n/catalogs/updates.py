# ruff: noqa: E501

from collections.abc import Mapping

from core.i18n.enums import LanguageEnum

LanguageMessages = Mapping[str, str]

MESSAGES: Mapping[LanguageEnum, LanguageMessages] = {
    LanguageEnum.RU: {
        "updates.seo.title": "Обновления",
        "updates.seo.description": "Публичный журнал изменений сайта.",
        "updates.hero.kicker": "Журнал изменений",
        "updates.hero.title": "Обновления сайта",
        "updates.hero.lead": "Крупные изменения сайта, сгруппированные по месяцам: публичный контент, "
        "админка, качество, безопасность и инфраструктура.",
        "updates.tag.frontend": "Frontend",
        "updates.tag.backend": "Backend",
        "updates.tag.content": "Контент",
        "updates.tag.seo": "SEO",
        "updates.tag.analytics": "Аналитика",
        "updates.tag.matrix": "Матрица",
        "updates.tag.infra": "Инфраструктура",
        "updates.tag.admin": "Админка",
        "updates.tag.auth": "Auth",
        "updates.tag.localization": "Локализация",
        "updates.tag.quality": "Качество",
        "updates.tag.security": "Безопасность",
        "updates.tag.delivery": "Доставка",
    },
    LanguageEnum.EN: {
        "updates.seo.title": "Updates",
        "updates.seo.description": "Public changelog for this site.",
        "updates.hero.kicker": "Changelog",
        "updates.hero.title": "Updates",
        "updates.hero.lead": "Major changes to the site, grouped by month: public content, admin "
        "workflows, quality, security, and infrastructure.",
        "updates.tag.frontend": "Frontend",
        "updates.tag.backend": "Backend",
        "updates.tag.content": "Content",
        "updates.tag.seo": "SEO",
        "updates.tag.analytics": "Analytics",
        "updates.tag.matrix": "Matrix",
        "updates.tag.infra": "Infrastructure",
        "updates.tag.admin": "Admin",
        "updates.tag.auth": "Auth",
        "updates.tag.localization": "Localization",
        "updates.tag.quality": "Quality",
        "updates.tag.security": "Security",
        "updates.tag.delivery": "Delivery",
    },
}
