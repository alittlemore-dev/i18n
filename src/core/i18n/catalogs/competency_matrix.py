# ruff: noqa: E501

from collections.abc import Mapping

from core.i18n.enums import LanguageEnum

LanguageMessages = Mapping[str, str]

MESSAGES: Mapping[LanguageEnum, LanguageMessages] = {
    LanguageEnum.RU: {
        "matrix.seo.title": "Матрица компетенций",
        "matrix.seo.description": "Матрица компетенций Junior/Middle/Senior разработчика.",
        "matrix.title": "Матрица компетенций",
        "matrix.suggestQuestion": "Предложить вопрос",
        "matrix.detailAria": "Детализация вопроса",
        "matrix.suggestion.title": "Предложить вопрос",
        "matrix.suggestion.placeholder": "Напишите вопрос, которого не хватает в матрице",
        "matrix.suggestion.submit": "Отправить",
        "matrix.suggestion.submitting": "Отправка...",
        "matrix.suggestion.sent": "Вопрос отправлен на рассмотрение.",
        "matrix.suggestion.error": "Не удалось отправить вопрос.",
        "matrix.suggestion.duplicate": "Такой вопрос уже есть в матрице или ожидает рассмотрения.",
        "matrix.suggestion.noSheets": "Нет публичных листов, для которых можно предложить вопрос.",
        "matrix.suggestion.sheetRequired": "Выберите публичный лист для вопроса.",
        "matrix.suggestion.quotaExceeded": "Лимит предложений на сегодня исчерпан.",
        "matrix.question.notFoundTitle": "Вопрос не найден",
        "matrix.question.notFoundDescription": "Вопрос матрицы недоступен или ещё не опубликован.",
        "matrix.question.backToMatrix": "Назад",
        "matrix.detail.suggestedBy": "Кто предложил:",
        "matrix.detail.openQuestion": "К вопросу",
        "matrix.filter.searchPlaceholder": "Поиск навыков и вопросов",
        "matrix.filter.clear": "Очистить",
        "matrix.filter.clearSearch": "Очистить поиск",
    },
    LanguageEnum.EN: {
        "matrix.seo.title": "Competency matrix",
        "matrix.seo.description": "Competency matrix for Junior/Middle/Senior developers.",
        "matrix.title": "Competency matrix",
        "matrix.suggestQuestion": "Suggest question",
        "matrix.detailAria": "Question details",
        "matrix.suggestion.title": "Suggest a question",
        "matrix.suggestion.placeholder": "Write the question that is missing from the matrix",
        "matrix.suggestion.submit": "Send",
        "matrix.suggestion.submitting": "Sending...",
        "matrix.suggestion.sent": "Question sent for review.",
        "matrix.suggestion.error": "Failed to send the question.",
        "matrix.suggestion.duplicate": "This question is already in the matrix or awaiting review.",
        "matrix.suggestion.noSheets": "There are no public sheets available for question suggestions.",
        "matrix.suggestion.sheetRequired": "Select a public sheet for the question.",
        "matrix.suggestion.quotaExceeded": "Today's suggestion limit has been reached.",
        "matrix.question.notFoundTitle": "Question not found",
        "matrix.question.notFoundDescription": "The matrix question is unavailable or unpublished.",
        "matrix.question.backToMatrix": "Back",
        "matrix.detail.suggestedBy": "Suggested by:",
        "matrix.detail.openQuestion": "To question",
        "matrix.filter.searchPlaceholder": "Search skills and questions",
        "matrix.filter.clear": "Clear",
        "matrix.filter.clearSearch": "Clear search",
    },
}
