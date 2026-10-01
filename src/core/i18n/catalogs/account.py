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
    },
}
