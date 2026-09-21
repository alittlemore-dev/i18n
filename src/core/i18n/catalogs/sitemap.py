from collections.abc import Mapping

from core.i18n.enums import LanguageEnum

LanguageMessages = Mapping[str, str]

MESSAGES: Mapping[LanguageEnum, LanguageMessages] = {
    LanguageEnum.RU: {
        "sitemap.seo.title": "Карта сайта",
        "sitemap.seo.description": "Карта сайта.",
        "sitemap.title": "Карта сайта",
        "sitemap.articles": "Опубликованные статьи",
        "sitemap.siteBuild": "Как устроен сайт",
        "sitemap.articlesEmpty": "Опубликованных статей пока нет.",
        "sitemap.articlesError": "Не удалось загрузить статьи.",
    },
    LanguageEnum.EN: {
        "sitemap.seo.title": "Sitemap",
        "sitemap.seo.description": "Sitemap.",
        "sitemap.title": "Sitemap",
        "sitemap.articles": "Published articles",
        "sitemap.siteBuild": "How this site is built",
        "sitemap.articlesEmpty": "No published articles yet.",
        "sitemap.articlesError": "Failed to load articles.",
    },
}
