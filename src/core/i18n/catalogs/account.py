from collections.abc import Mapping

from core.i18n.enums import LanguageEnum

LanguageMessages = Mapping[str, str]

MESSAGES: Mapping[LanguageEnum, LanguageMessages] = {
    LanguageEnum.RU: {
        "account.title": "Личный кабинет",
        "account.navigation": "Разделы профиля",
        "account.sidePanel.open": "Открыть разделы профиля",
        "account.sidePanel.close": "Закрыть разделы профиля",
        "account.profile.title": "Профиль",
        "account.settings.general": "Общие",
        "account.settings.appearance": "Внешний вид",
        "account.settings.telegram": "Telegram",
        "account.telegram.title": "Telegram-бот",
        "account.telegram.unavailable": (
            "Бот пока не настроен на сервере. Подключение станет доступно после настройки бота."
        ),
        "account.telegram.connecting": (
            "Подключаемся к Telegram. Настройки станут доступны после подключения."
        ),
        "account.telegram.failed": (
            "Не удалось подключиться к Telegram. Настройки временно недоступны. "
            "Подключение будет проверено повторно автоматически."
        ),
        "account.telegram.enabled": "Разрешить подключение Telegram-аккаунтов",
        "account.telegram.notify": "Отправлять уведомления через бота",
        "account.telegram.notificationSettings": "Настройки уведомлений",
        "account.telegram.notifyBirthday": "Дни рождения",
        "account.telegram.notifyMemorableDate": "Памятные даты",
        "account.telegram.notifyFinanceTransaction": "Новые финансовые операции других участников",
        "account.telegram.notifyFinanceLimit": "Превышение лимитов расходов",
        "account.telegram.notificationLanguage": "Язык уведомлений",
        "account.telegram.saveNotifications": "Сохранить уведомления",
        "account.telegram.inviteHint": (
            "Создайте одноразовую ссылку и отправьте её участнику. "
            "Подключение потребует вашего подтверждения."
        ),
        "account.telegram.label": "Имя участника",
        "account.telegram.labelRequired": "Введите имя участника (до 100 символов).",
        "account.telegram.createInvite": "Создать новую ссылку",
        "account.telegram.linkOnce": "Сохраните ссылку сейчас: позже она не будет показана снова.",
        "account.telegram.expires": "Действует до",
        "account.telegram.cancelInvite": "Отменить ссылку",
        "account.telegram.connections": "Telegram-аккаунты",
        "account.telegram.noConnections": "Подключённых аккаунтов и запросов пока нет.",
        "account.telegram.state": "Статус",
        "account.telegram.state.pending": "Ожидает подтверждения",
        "account.telegram.state.active": "Подключён",
        "account.telegram.state.revoked": "Отключён",
        "account.telegram.state.blocked": "Заблокирован",
        "account.telegram.approve": "Подтвердить",
        "account.telegram.reject": "Отклонить",
        "account.telegram.revoke": "Отключить",
        "account.telegram.block": "Заблокировать",
        "account.telegram.unblock": "Снять блокировку",
        "account.telegram.rename": "Переименовать",
        "account.telegram.saveLabel": "Сохранить имя",
        "account.telegram.loadFailed": "Не удалось загрузить Telegram-настройки.",
        "account.telegram.actionFailed": "Не удалось выполнить действие. Повторите попытку.",
        "account.telegram.confirmCancel": "Отменить эту ссылку?",
        "account.telegram.confirm.revoke": "Отключить этого участника?",
        "account.telegram.confirm.block": (
            "Заблокировать Telegram-аккаунт? Он не сможет подключиться снова."
        ),
        "account.telegram.confirm.unblock": (
            "Снять блокировку? Для повторного подключения понадобится новая ссылка."
        ),
        "account.settings.theme": "Тема",
        "account.settings.timeZone": "Часовой пояс",
        "account.settings.timeZoneDevice": "Использовать часовой пояс устройства",
        "account.settings.timeZoneHint": (
            "Определяет время в календаре, часовой пояс новых и повторяющихся событий "
            "и будущих напоминаний Telegram. Разовые события сохраняют момент времени, "
            "события на весь день — дату."
        ),
        "account.settings.autosave": "Изменения сохраняются автоматически.",
        "account.settings.saving": "Сохранение…",
        "account.settings.loadFailed": "Не удалось загрузить настройки.",
        "account.profile.edit": "Редактировать",
        "account.profile.fullName": "ФИО",
        "account.profile.firstName": "Имя",
        "account.profile.lastName": "Фамилия",
        "account.profile.middleName": "Отчество",
        "account.profile.gender": "Пол",
        "account.profile.gender.male": "Мужской",
        "account.profile.gender.female": "Женский",
        "account.profile.username": "Имя пользователя",
        "account.profile.changeAvatar": "Заменить аватар",
        "account.profile.removeAvatar": "Удалить аватар",
        "account.profile.avatarAlt": "Аватар пользователя {username}",
        "account.profile.loading": "Загрузка профиля…",
        "account.profile.loadFailed": "Не удалось загрузить профиль.",
        "account.profile.retry": "Повторить",
        "account.profile.saveSuccess": "Профиль сохранён.",
        "account.profile.avatarSaveSuccess": "Аватар обновлён.",
        "account.profile.avatarRemoveSuccess": "Аватар удалён.",
        "account.profile.saveFailed": "Не удалось сохранить профиль.",
        "account.profile.avatarFailed": "Не удалось обновить аватар.",
        "account.profile.invalidAvatarType": "Выберите изображение PNG, JPEG или WebP.",
        "account.profile.avatarTooLarge": "Размер изображения не должен превышать 5 МБ.",
        "account.profile.invalid": "Исправьте поля формы.",
        "account.profile.noChanges": "Изменений для сохранения нет.",
        "account.apiAccess.title": "Доступ к API",
        "account.apiAccess.description": (
            "Создавайте отдельные именованные токены для скриптов и AI-агентов. "
            "Токен действует от вашего имени с выбранными полномочиями и текущей "
            "ролью. Полномочия и срок неизменяемы; токен можно отозвать."
        ),
        "account.apiAccess.create": "Создать токен",
        "account.apiAccess.name": "Название",
        "account.apiAccess.duration": "Срок действия",
        "account.apiAccess.expiresAt": "Истекает",
        "account.apiAccess.permissions": "Полномочия",
        "account.apiAccess.permissionsHint": (
            "Выберите только нужные операции. «Все доступные» сохраняет текущий "
            "список конкретных полномочий; будущие полномочия не добавляются."
        ),
        "account.apiAccess.selectAll": "Все доступные",
        "account.apiAccess.selectNone": "Снять выбор",
        "account.apiAccess.noPermissions": "Для вашей роли нет доступных полномочий.",
        "account.apiAccess.password": "Текущий пароль",
        "account.apiAccess.tokens": "Ваши токены",
        "account.apiAccess.status": "Статус",
        "account.apiAccess.createdAt": "Создан",
        "account.apiAccess.lastUsedAt": "Последнее использование",
        "account.apiAccess.neverUsed": "Ещё не использован",
        "account.apiAccess.show": "Показать",
        "account.apiAccess.hide": "Скрыть",
        "account.apiAccess.copy": "Копировать",
        "account.apiAccess.revoke": "Отозвать",
        "account.apiAccess.empty": "Токенов пока нет.",
        "account.apiAccess.loadFailed": "Не удалось загрузить токены и полномочия.",
        "account.apiAccess.invalid": "Укажите название, пароль и хотя бы одно полномочие.",
        "account.apiAccess.invalidExpiry": (
            "Выберите будущую дату и время не позднее чем через 365 дней."
        ),
        "account.apiAccess.created": (
            "Токен создан. Нажмите «Показать» и снова подтвердите пароль."
        ),
        "account.apiAccess.createFailed": (
            "Не удалось создать токен. Проверьте пароль, срок и полномочия."
        ),
        "account.apiAccess.passwordRequired": "Введите текущий пароль для этого действия.",
        "account.apiAccess.shown": "Токен показан. Скройте его после использования.",
        "account.apiAccess.hidden": "Токен скрыт.",
        "account.apiAccess.copied": "Токен скопирован.",
        "account.apiAccess.copyFailed": (
            "Не удалось скопировать токен. Повторите действие с паролем."
        ),
        "account.apiAccess.revealFailed": (
            "Не удалось получить токен. Проверьте пароль и статус токена."
        ),
        "account.apiAccess.revoked": "Токен отозван.",
        "account.apiAccess.revokeFailed": "Не удалось отозвать токен.",
        "account.apiAccess.docsIntro": "Доступные операции описаны в",
        "account.apiAccess.docs": "единой документации API",
        "account.apiAccess.permissionCount": "Полномочий: {count}",
        "account.apiAccess.permissionSelection": "Выбрано {selected} из {total}",
        "account.apiAccess.selectedPermissions": "Выбрано полномочий: {count}",
        "account.apiAccess.service.auth": "Аккаунт и безопасность",
        "account.apiAccess.service.workspace": "Личное пространство",
        "account.apiAccess.service.competency": "Матрица компетенций",
        "account.apiAccess.examples": "Примеры использования",
        "account.apiAccess.requiredPermission": "Нужное полномочие:",
        "account.apiAccess.exampleTokenHint": (
            "Замените <YOUR_API_TOKEN> своим токеном. Если пример содержит JSON, "
            "сохраните его в файл с указанным именем. Данные в примерах вымышленные."
        ),
        "account.apiAccess.example.profile.title": "Получить данные своего профиля",
        "account.apiAccess.example.profile.summary": "Личные данные для скрипта или нейросети",
        "account.apiAccess.example.profile.hint": (
            "Попросите инструмент получить ваш профиль, чтобы подставить имя и "
            "другие данные аккаунта в документ. Запрос возвращает текущего пользователя."
        ),
        "account.apiAccess.example.resumeRead.title": "Проанализировать свои резюме",
        "account.apiAccess.example.resumeRead.summary": "Чтение без изменения данных",
        "account.apiAccess.example.resumeRead.hint": (
            "Попросите нейросеть загрузить ваши резюме и предложить улучшения или "
            "сравнить опыт с вакансией. Запрос получает первую страницу списка; "
            "параметры page и pageSize управляют страницей и её размером."
        ),
        "account.apiAccess.example.resumeImport.title": "Импортировать резюме",
        "account.apiAccess.example.resumeImport.summary": "Из текста или другого формата в JSON",
        "account.apiAccess.example.resumeImport.hint": (
            "Дайте нейросети текст своего резюме и попросите преобразовать его в "
            "структуру ниже. Затем отправьте JSON: новое резюме появится в личном пространстве."
        ),
        "account.apiAccess.example.event.title": "Добавить событие в календарь",
        "account.apiAccess.example.event.summary": "Собеседование, встреча или напоминание",
        "account.apiAccess.example.event.hint": (
            "Попросите инструмент превратить договорённость о встрече в событие. "
            "Укажите название, начало и конец. В примере время задано в UTC, "
            "без повторения; замените даты и описание своими."
        ),
        "account.apiAccess.status.active": "Активен",
        "account.apiAccess.status.expired": "Истёк",
        "account.apiAccess.status.revoked": "Отозван",
        "account.apiAccess.duration.1h": "1 час",
        "account.apiAccess.duration.1d": "1 день",
        "account.apiAccess.duration.7d": "7 дней",
        "account.apiAccess.duration.30d": "30 дней",
        "account.apiAccess.duration.90d": "90 дней",
        "account.apiAccess.duration.365d": "365 дней",
        "account.apiAccess.duration.custom": "Своя дата и время",
        "account.apiAccess.action.read": "Чтение",
        "account.apiAccess.action.create": "Создание и импорт",
        "account.apiAccess.action.update": "Изменение",
        "account.apiAccess.action.delete": "Удаление",
        "account.apiAccess.action.publish": "Публикация",
        "account.apiAccess.action.password": "Смена пароля",
        "account.apiAccess.action.role": "Изменение роли",
        "account.apiAccess.action.activate": "Активация",
        "account.apiAccess.action.deactivate": "Деактивация",
        "account.apiAccess.action.revoke": "Отзыв сессий",
        "account.apiAccess.action.manage": "Управление",
        "account.apiAccess.action.manage_access": "Управление доступом",
        "account.apiAccess.action.record_view": "Запись просмотра",
        "account.apiAccess.action.suggest": "Предложение вопроса",
        "account.apiAccess.domain.auth.account": "Мой аккаунт",
        "account.apiAccess.domain.auth.accounts": "Аккаунты",
        "account.apiAccess.domain.auth.sessions": "Сессии",
        "account.apiAccess.domain.auth.tools": "Инструменты авторизации",
        "account.apiAccess.domain.workspace.resumes": "Резюме",
        "account.apiAccess.domain.workspace.files": "Файлы пространства",
        "account.apiAccess.domain.workspace.knowledge": "База знаний",
        "account.apiAccess.domain.workspace.events": "События",
        "account.apiAccess.domain.workspace.calendar": "Календарь",
        "account.apiAccess.domain.workspace.finance": "Финансы",
        "account.apiAccess.domain.workspace.vault": "Хранилище",
        "account.apiAccess.domain.workspace.important_info": "Важная информация",
        "account.apiAccess.domain.workspace.wiki_links": "Ссылки пространства",
        "account.apiAccess.domain.workspace.telegram": "Telegram",
        "account.apiAccess.domain.workspace.tools": "Инструменты пространства",
        "account.apiAccess.domain.competency.articles": "Статьи",
        "account.apiAccess.domain.competency.matrix": "Матрица компетенций",
        "account.apiAccess.domain.competency.files": "Файлы контента",
        "account.apiAccess.domain.competency.wiki_links": "Ссылки контента",
        "account.apiAccess.domain.competency.tools": "Инструменты контента",
        "account.apiAccess.dateTime.placeholder": "ДД.ММ.ГГГГ ЧЧ:ММ",
        "account.apiAccess.dateTime.open": "Выбрать дату и время",
        "account.apiAccess.dateTime.change": "Изменить дату и время",
        "account.apiAccess.dateTime.hour": "Час",
        "account.apiAccess.dateTime.minute": "Минута",
        "account.apiAccess.dateTime.timeFormat": "Время в формате ЧЧ:ММ",
        "account.apiAccess.dateTime.now": "Сейчас",
    },
    LanguageEnum.EN: {
        "account.title": "Account",
        "account.navigation": "Profile sections",
        "account.sidePanel.open": "Open profile sections",
        "account.sidePanel.close": "Close profile sections",
        "account.profile.title": "Profile",
        "account.settings.general": "General",
        "account.settings.appearance": "Appearance",
        "account.settings.telegram": "Telegram",
        "account.telegram.title": "Telegram bot",
        "account.telegram.unavailable": (
            "The bot is not configured on the server yet. "
            "Connections will be available after setup."
        ),
        "account.telegram.connecting": (
            "Connecting to Telegram. Settings will be available once connected."
        ),
        "account.telegram.failed": (
            "Could not connect to Telegram. Settings are temporarily unavailable. "
            "The connection will be checked again automatically."
        ),
        "account.telegram.enabled": "Allow Telegram account connections",
        "account.telegram.notify": "Send notifications through the bot",
        "account.telegram.notificationSettings": "Notification settings",
        "account.telegram.notifyBirthday": "Birthdays",
        "account.telegram.notifyMemorableDate": "Memorable dates",
        "account.telegram.notifyFinanceTransaction": (
            "New financial transactions by other participants"
        ),
        "account.telegram.notifyFinanceLimit": "Expense limit overruns",
        "account.telegram.notificationLanguage": "Notification language",
        "account.telegram.saveNotifications": "Save notifications",
        "account.telegram.inviteHint": (
            "Create a one-time link and share it with a participant. "
            "You must approve the connection."
        ),
        "account.telegram.label": "Participant name",
        "account.telegram.labelRequired": "Enter a participant name (up to 100 characters).",
        "account.telegram.createInvite": "Create a new link",
        "account.telegram.linkOnce": "Save this link now; it will not be shown again.",
        "account.telegram.expires": "Expires",
        "account.telegram.cancelInvite": "Cancel link",
        "account.telegram.connections": "Telegram accounts",
        "account.telegram.noConnections": "No connected accounts or requests yet.",
        "account.telegram.state": "Status",
        "account.telegram.state.pending": "Awaiting approval",
        "account.telegram.state.active": "Connected",
        "account.telegram.state.revoked": "Disconnected",
        "account.telegram.state.blocked": "Blocked",
        "account.telegram.approve": "Approve",
        "account.telegram.reject": "Reject",
        "account.telegram.revoke": "Disconnect",
        "account.telegram.block": "Block",
        "account.telegram.unblock": "Unblock",
        "account.telegram.rename": "Rename",
        "account.telegram.saveLabel": "Save name",
        "account.telegram.loadFailed": "Could not load Telegram settings.",
        "account.telegram.actionFailed": "The action failed. Try again.",
        "account.telegram.confirmCancel": "Cancel this link?",
        "account.telegram.confirm.revoke": "Disconnect this participant?",
        "account.telegram.confirm.block": (
            "Block this Telegram account? It will not be able to reconnect."
        ),
        "account.telegram.confirm.unblock": (
            "Unblock this account? A new link will be needed to reconnect."
        ),
        "account.settings.theme": "Theme",
        "account.settings.timeZone": "Time zone",
        "account.settings.timeZoneDevice": "Use device time zone",
        "account.settings.timeZoneHint": (
            "Controls calendar display, the time zone for new and recurring events, "
            "and future Telegram reminders. One-off events keep their instant, "
            "and all-day events keep their date."
        ),
        "account.settings.autosave": "Changes are saved automatically.",
        "account.settings.saving": "Saving…",
        "account.settings.loadFailed": "Could not load settings.",
        "account.profile.edit": "Edit",
        "account.profile.fullName": "Full name",
        "account.profile.firstName": "First name",
        "account.profile.lastName": "Last name",
        "account.profile.middleName": "Middle name",
        "account.profile.gender": "Gender",
        "account.profile.gender.male": "Male",
        "account.profile.gender.female": "Female",
        "account.profile.username": "Username",
        "account.profile.changeAvatar": "Change avatar",
        "account.profile.removeAvatar": "Remove avatar",
        "account.profile.avatarAlt": "Avatar of {username}",
        "account.profile.loading": "Loading profile…",
        "account.profile.loadFailed": "Failed to load the profile.",
        "account.profile.retry": "Retry",
        "account.profile.saveSuccess": "Profile saved.",
        "account.profile.avatarSaveSuccess": "Avatar updated.",
        "account.profile.avatarRemoveSuccess": "Avatar removed.",
        "account.profile.saveFailed": "Failed to save the profile.",
        "account.profile.avatarFailed": "Failed to update the avatar.",
        "account.profile.invalidAvatarType": "Choose a PNG, JPEG, or WebP image.",
        "account.profile.avatarTooLarge": "The image must be no larger than 5 MB.",
        "account.profile.invalid": "Fix the form fields.",
        "account.profile.noChanges": "There are no changes to save.",
        "account.apiAccess.title": "API access",
        "account.apiAccess.description": (
            "Create separate named tokens for scripts and AI agents. Each token "
            "acts on your behalf with its selected permissions and your current "
            "role. Permissions and expiration cannot be changed; you can revoke "
            "the token."
        ),
        "account.apiAccess.create": "Create token",
        "account.apiAccess.name": "Name",
        "account.apiAccess.duration": "Lifetime",
        "account.apiAccess.expiresAt": "Expires",
        "account.apiAccess.permissions": "Permissions",
        "account.apiAccess.permissionsHint": (
            "Select only the operations you need. “All available” saves the "
            "current list of concrete permissions; future permissions are not "
            "added."
        ),
        "account.apiAccess.selectAll": "All available",
        "account.apiAccess.selectNone": "Clear selection",
        "account.apiAccess.noPermissions": "No permissions are available for your role.",
        "account.apiAccess.password": "Current password",
        "account.apiAccess.tokens": "Your tokens",
        "account.apiAccess.status": "Status",
        "account.apiAccess.createdAt": "Created",
        "account.apiAccess.lastUsedAt": "Last used",
        "account.apiAccess.neverUsed": "Never used",
        "account.apiAccess.show": "Show",
        "account.apiAccess.hide": "Hide",
        "account.apiAccess.copy": "Copy",
        "account.apiAccess.revoke": "Revoke",
        "account.apiAccess.empty": "No tokens yet.",
        "account.apiAccess.loadFailed": "Could not load tokens and permissions.",
        "account.apiAccess.invalid": "Enter a name, password and at least one permission.",
        "account.apiAccess.invalidExpiry": "Choose a future date and time within 365 days.",
        "account.apiAccess.created": (
            "Token created. Select “Show” and confirm your password again."
        ),
        "account.apiAccess.createFailed": (
            "Could not create the token. Check your password, expiration and permissions."
        ),
        "account.apiAccess.passwordRequired": "Enter your current password for this action.",
        "account.apiAccess.shown": "Token shown. Hide it after use.",
        "account.apiAccess.hidden": "Token hidden.",
        "account.apiAccess.copied": "Token copied.",
        "account.apiAccess.copyFailed": "Could not copy the token. Retry with your password.",
        "account.apiAccess.revealFailed": (
            "Could not retrieve the token. Check your password and the token status."
        ),
        "account.apiAccess.revoked": "Token revoked.",
        "account.apiAccess.revokeFailed": "Could not revoke the token.",
        "account.apiAccess.docsIntro": "Available operations are described in the",
        "account.apiAccess.docs": "unified API documentation",
        "account.apiAccess.permissionCount": "Permissions: {count}",
        "account.apiAccess.permissionSelection": "Selected {selected} of {total}",
        "account.apiAccess.selectedPermissions": "Selected permissions: {count}",
        "account.apiAccess.service.auth": "Account and security",
        "account.apiAccess.service.workspace": "Personal workspace",
        "account.apiAccess.service.competency": "Competency matrix",
        "account.apiAccess.examples": "Usage examples",
        "account.apiAccess.requiredPermission": "Required permission:",
        "account.apiAccess.exampleTokenHint": (
            "Replace <YOUR_API_TOKEN> with your token. If an example includes JSON, "
            "save it in a file with the given name. All example data is fictional."
        ),
        "account.apiAccess.example.profile.title": "Get your profile",
        "account.apiAccess.example.profile.summary": "Personal details for a script or AI tool",
        "account.apiAccess.example.profile.hint": (
            "Ask a tool to load your profile and use your name and other account "
            "details in a document. This request returns the current user."
        ),
        "account.apiAccess.example.resumeRead.title": "Analyze your resumes",
        "account.apiAccess.example.resumeRead.summary": "Read without changing your data",
        "account.apiAccess.example.resumeRead.hint": (
            "Ask an AI tool to load your resumes and suggest improvements or "
            "compare your experience with a job description. This request gets the "
            "first page; page and pageSize control pagination."
        ),
        "account.apiAccess.example.resumeImport.title": "Import a resume",
        "account.apiAccess.example.resumeImport.summary": "Convert text or another format to JSON",
        "account.apiAccess.example.resumeImport.hint": (
            "Give an AI tool your resume text and ask it to convert it to the "
            "structure below. Submit the JSON to add a resume to your personal workspace."
        ),
        "account.apiAccess.example.event.title": "Add a calendar event",
        "account.apiAccess.example.event.summary": "An interview, meeting or reminder",
        "account.apiAccess.example.event.hint": (
            "Ask a tool to turn a meeting arrangement into an event. Set its "
            "title, start and end. This example uses UTC with no recurrence; "
            "replace the dates and description with your own."
        ),
        "account.apiAccess.status.active": "Active",
        "account.apiAccess.status.expired": "Expired",
        "account.apiAccess.status.revoked": "Revoked",
        "account.apiAccess.duration.1h": "1 hour",
        "account.apiAccess.duration.1d": "1 day",
        "account.apiAccess.duration.7d": "7 days",
        "account.apiAccess.duration.30d": "30 days",
        "account.apiAccess.duration.90d": "90 days",
        "account.apiAccess.duration.365d": "365 days",
        "account.apiAccess.duration.custom": "Custom date and time",
        "account.apiAccess.action.read": "Read",
        "account.apiAccess.action.create": "Create and import",
        "account.apiAccess.action.update": "Update",
        "account.apiAccess.action.delete": "Delete",
        "account.apiAccess.action.publish": "Publish",
        "account.apiAccess.action.password": "Change password",
        "account.apiAccess.action.role": "Change role",
        "account.apiAccess.action.activate": "Activate",
        "account.apiAccess.action.deactivate": "Deactivate",
        "account.apiAccess.action.revoke": "Revoke sessions",
        "account.apiAccess.action.manage": "Manage",
        "account.apiAccess.action.manage_access": "Manage access",
        "account.apiAccess.action.record_view": "Record view",
        "account.apiAccess.action.suggest": "Suggest question",
        "account.apiAccess.domain.auth.account": "My account",
        "account.apiAccess.domain.auth.accounts": "Accounts",
        "account.apiAccess.domain.auth.sessions": "Sessions",
        "account.apiAccess.domain.auth.tools": "Authentication tools",
        "account.apiAccess.domain.workspace.resumes": "Resumes",
        "account.apiAccess.domain.workspace.files": "Workspace files",
        "account.apiAccess.domain.workspace.knowledge": "Knowledge base",
        "account.apiAccess.domain.workspace.events": "Events",
        "account.apiAccess.domain.workspace.calendar": "Calendar",
        "account.apiAccess.domain.workspace.finance": "Finance",
        "account.apiAccess.domain.workspace.vault": "Vault",
        "account.apiAccess.domain.workspace.important_info": "Important information",
        "account.apiAccess.domain.workspace.wiki_links": "Workspace links",
        "account.apiAccess.domain.workspace.telegram": "Telegram",
        "account.apiAccess.domain.workspace.tools": "Workspace tools",
        "account.apiAccess.domain.competency.articles": "Articles",
        "account.apiAccess.domain.competency.matrix": "Competency matrix",
        "account.apiAccess.domain.competency.files": "Content files",
        "account.apiAccess.domain.competency.wiki_links": "Content links",
        "account.apiAccess.domain.competency.tools": "Content tools",
        "account.apiAccess.dateTime.placeholder": "MM/DD/YYYY HH:MM",
        "account.apiAccess.dateTime.open": "Choose date and time",
        "account.apiAccess.dateTime.change": "Change date and time",
        "account.apiAccess.dateTime.hour": "Hour",
        "account.apiAccess.dateTime.minute": "Minute",
        "account.apiAccess.dateTime.timeFormat": "Time in HH:MM format",
        "account.apiAccess.dateTime.now": "Now",
    },
}
