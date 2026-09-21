from collections.abc import Mapping

from core.i18n.enums import LanguageEnum

LanguageMessages = Mapping[str, str]

MESSAGES: Mapping[LanguageEnum, LanguageMessages] = {
    LanguageEnum.RU: {
        "articles.seo.title": "Статьи",
        "articles.seo.description": "Статьи и короткие материалы.",
        "articles.activeTag": "Тег: {name}",
        "articles.filters.searchPlaceholder": "Заголовок или текст",
        "articles.filters.resetTag": "Сбросить тег",
        "articles.views": "{count} просмотров",
        "articles.folders": "Папки",
        "articles.sidePanel.open": "Открыть папки",
        "articles.sidePanel.close": "Скрыть папки",
        "articles.emptyTree": "Статей пока нет.",
        "articles.reactions": "Реакции",
        "articles.pagination": "Пагинация статей",
        "articles.notify.reactionError": "Не удалось сохранить реакцию.",
    },
    LanguageEnum.EN: {
        "articles.seo.title": "Articles",
        "articles.seo.description": "Articles and short materials.",
        "articles.activeTag": "Tag: {name}",
        "articles.filters.searchPlaceholder": "Title or text",
        "articles.filters.resetTag": "Reset tag",
        "articles.views": "{count} views",
        "articles.folders": "Folders",
        "articles.sidePanel.open": "Open folders",
        "articles.sidePanel.close": "Hide folders",
        "articles.emptyTree": "No articles yet.",
        "articles.reactions": "Reactions",
        "articles.pagination": "Articles pagination",
        "articles.notify.reactionError": "Failed to save reaction.",
    },
}
