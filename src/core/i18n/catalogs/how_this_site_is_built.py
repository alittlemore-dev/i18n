# ruff: noqa: E501

from collections.abc import Mapping

from core.i18n.enums import LanguageEnum

LanguageMessages = Mapping[str, str]

MESSAGES: Mapping[LanguageEnum, LanguageMessages] = {
    LanguageEnum.RU: {
        "siteBuild.seo.title": "Как устроен сайт",
        "siteBuild.seo.description": "Инженерный разбор устройства портфолио и платформы публикаций.",
        "siteBuild.hero.kicker": "Инженерный разбор",
        "siteBuild.hero.title": "Как устроен этот сайт",
        "siteBuild.hero.lead": "Инженерный разбор production-подхода к портфолио и публикационной "
        "платформе: архитектура, локализация, управление контентом, качество, "
        "безопасность и инфраструктура.",
        "siteBuild.hero.sourceCode": "Исходный код",
        "siteBuild.hero.matrixLink": "Открыть матрицу",
        "siteBuild.hero.logoAlt": "Логотип сайта",
        "siteBuild.problem.title": "Задача",
        "siteBuild.problem.body": "Сайт объединяет статьи, матрицу компетенций и разбор собственной "
        "архитектуры. Он должен быть полезным читателям, удобным для автора и "
        "одновременно показывать реальные инженерные решения, а не только "
        "список технологий.",
        "siteBuild.architecture.title": "Архитектура",
        "siteBuild.architecture.backendTitle": "Backend",
        "siteBuild.architecture.backendBody": "Litestar, SQLAlchemy, Dishka и PostgreSQL образуют "
        "API-first backend с явными границами между доменной "
        "логикой, HTTP-слоем, инфраструктурой и хранением. Статьи, "
        "матрица компетенций, управление командой и служебные "
        "инструменты сохраняют собственные контракты, а общие "
        "механизмы остаются ниже транспортной границы.",
        "siteBuild.architecture.frontendTitle": "Frontend",
        "siteBuild.architecture.frontendBody": "Angular hybrid SSR/CSR и backend-driven i18n дают SEO для "
        "публичных страниц, а read-only матрица и статьи отделены "
        "от protected workspaces: контентом управляют владелец, "
        "администраторы и модераторы, а командой — владелец и "
        "администраторы.",
        "siteBuild.architecture.infraTitle": "Infrastructure",
        "siteBuild.architecture.infraBody": "nginx, Docker, MinIO с S3-compatible media storage, Valkey и "
        "TaskIQ разделяют edge routing, файлы, кэш, фоновые задачи и "
        "runtime frontend/backend контейнеров, а публичный трафик "
        "переключается между blue/green слотами после health checks. "
        "Для public-media PostgreSQL отслеживает жизненный цикл "
        "ссылок, а фоновая TaskIQ-задача безопасно удаляет "
        "неиспользуемые объекты после настраиваемого периода хранения "
        "и повторяет неудачные операции. Edge nginx "
        "самовосстанавливается после устойчивого отказа локального "
        "liveness endpoint и использует restart policy для "
        "перезапуска Docker или VPS.",
        "siteBuild.architecture.agentTitle": "Безопасный AI-доступ",
        "siteBuild.architecture.agentBody": "Ограниченный Agent REST-контур смонтирован в основном "
        "Litestar-приложении без отдельного процесса и Unix-сокета. "
        "Приватную границу сохраняет отдельный WireGuard-bound nginx "
        "mTLS-listener с точным allowlist; публичный listener "
        "возвращает 404 для внутреннего пути и удаляет поддельный "
        "certificate header. Локальный stdio MCP-мост открывает "
        "ограниченный набор Draft-only операций без publish, generic "
        "CRUD, SQL, shell или URL fetch. Упрощение осознанно "
        "оставляет общими с backend процесс, роль БД, секреты и "
        "доступность: изоляция private application network и доверие "
        "к nginx остаются частью boundary.",
        "siteBuild.decisions.title": "Инженерные решения",
        "siteBuild.decision.cleanArchitecture": "Clean Architecture: доменная логика не зависит от "
        "Litestar, SQLAlchemy или внешних сервисов.",
        "siteBuild.decision.localizedContent": "RU/EN локализация разделена на UI-каталог и контентные "
        "поля, чтобы не смешивать интерфейс со статьями и "
        "матрицей.",
        "siteBuild.decision.privacyAnalytics": "Privacy-safe аналитика считает просмотры и реакции без "
        "cookies, raw IP, user-agent или сторонних "
        "идентификаторов.",
        "siteBuild.decision.deployManifest": "Деплой оформлен как управляемый release process с ручным "
        "запуском: runtime-конфигурация собирается из manifest, CI "
        "quality gates отделены от deploy workflow, ручное "
        "подтверждение production environment остаётся явным, а "
        "blue/green переключение с health checks снижает риск "
        "релиза.",
        "siteBuild.quality.title": "Качество и эксплуатация",
        "siteBuild.quality.body": "Качество держится на коротких проверках: стиль, типы, unit/integration "
        "тесты, безопасность, SSR smoke, производительность и SQL-планы. Они "
        "остаются CI evidence перед релизом, а production deploy запускается "
        "вручную и переключает blue/green трафик только после health checks. В "
        "эксплуатации фоновые задачи, кэш, файлы и runtime контейнеры разделены "
        "по ответственности; публичные ассеты обслуживаются с CSP и immutable "
        "caching.",
        "siteBuild.next.title": "Что дальше",
        "siteBuild.next.body": "Ближайшие направления: RSS/Atom, публичный roadmap и дальнейшая работа "
        "над наблюдаемостью, производительностью и качеством контента.",
        "siteBuild.next.articlesLink": "Перейти к статьям",
    },
    LanguageEnum.EN: {
        "siteBuild.seo.title": "How this site is built",
        "siteBuild.seo.description": "An engineering case study about this portfolio and publishing "
        "platform.",
        "siteBuild.hero.kicker": "Engineering case study",
        "siteBuild.hero.title": "How this site is built",
        "siteBuild.hero.lead": "Engineering case study of a production-minded portfolio and publishing "
        "platform: architecture, localization, content authoring, quality, "
        "security, and infrastructure.",
        "siteBuild.hero.sourceCode": "Source code",
        "siteBuild.hero.matrixLink": "Open the matrix",
        "siteBuild.hero.logoAlt": "Site logo",
        "siteBuild.problem.title": "Problem",
        "siteBuild.problem.body": "The site combines articles, a competency matrix, and architecture "
        "notes. It needs to help readers, stay comfortable for authoring, and "
        "demonstrate real engineering decisions instead of only listing "
        "technologies.",
        "siteBuild.architecture.title": "Architecture",
        "siteBuild.architecture.backendTitle": "Backend",
        "siteBuild.architecture.backendBody": "Litestar, SQLAlchemy, Dishka, and PostgreSQL form an "
        "API-first backend with explicit boundaries between domain "
        "logic, HTTP, infrastructure, and storage. Articles, the "
        "competency matrix, team administration, and operational "
        "tools keep their own contracts, while shared mechanisms "
        "stay below the transport boundary.",
        "siteBuild.architecture.frontendTitle": "Frontend",
        "siteBuild.architecture.frontendBody": "Angular hybrid SSR/CSR and backend-driven i18n provide "
        "SEO for public pages, while read-only matrix and article "
        "surfaces stay separate from protected workspaces: owner, "
        "admins, and moderators manage content, while owner and "
        "admins govern the team.",
        "siteBuild.architecture.infraTitle": "Infrastructure",
        "siteBuild.architecture.infraBody": "nginx, Docker, MinIO with S3-compatible media storage, "
        "Valkey, and TaskIQ separate edge routing, files, cache, "
        "background jobs, and frontend/backend container runtimes, "
        "while public traffic switches between blue/green slots only "
        "after health checks pass. For public media, PostgreSQL "
        "tracks the reference lifecycle, while a background TaskIQ "
        "job safely removes unused objects after a configurable "
        "retention period and retries failed operations. The edge "
        "nginx self-recovers after a sustained local liveness failure "
        "and uses a restart policy for Docker daemon or VPS restarts.",
        "siteBuild.architecture.agentTitle": "Safe AI access",
        "siteBuild.architecture.agentBody": "A bounded Agent REST surface is mounted in the main Litestar "
        "application without a separate process or Unix socket. A "
        "dedicated WireGuard-bound nginx mTLS listener preserves the "
        "private boundary with an exact allowlist; the public "
        "listener returns 404 for the internal path and strips forged "
        "certificate headers. A local stdio MCP bridge exposes an "
        "allowlisted Draft-only authoring surface with no publish, "
        "generic CRUD, SQL, shell, or URL fetch. The simplification "
        "intentionally shares the backend process, DB role, secrets, "
        "and availability: private application-network isolation and "
        "trust in nginx remain part of the boundary.",
        "siteBuild.decisions.title": "Engineering decisions",
        "siteBuild.decision.cleanArchitecture": "Clean Architecture keeps domain logic independent from "
        "Litestar, SQLAlchemy, and external services.",
        "siteBuild.decision.localizedContent": "RU/EN localization is split between the UI catalog and "
        "content fields, so interface text is not mixed with "
        "articles and matrix content.",
        "siteBuild.decision.privacyAnalytics": "Privacy-safe analytics count views and reactions without "
        "cookies, raw IPs, user-agent strings, or third-party "
        "identifiers.",
        "siteBuild.decision.deployManifest": "Deployment is treated as a controlled release process with "
        "a manual trigger: runtime configuration is rendered from a "
        "manifest, CI quality gates are decoupled from the deploy "
        "workflow, manual approval on the production environment "
        "remains explicit, and blue/green switching with health "
        "checks lowers rollout risk.",
        "siteBuild.quality.title": "Quality and operations",
        "siteBuild.quality.body": "Quality is covered by short checks: style, types, unit/integration "
        "tests, security, SSR smoke, performance, and SQL plans. They remain CI "
        "release evidence, while production deploy runs manually and switches "
        "blue/green traffic only after health checks pass. In operations, "
        "background jobs, cache, files, and runtime containers have separate "
        "responsibilities; public assets are served with CSP and immutable "
        "caching.",
        "siteBuild.next.title": "What is next",
        "siteBuild.next.body": "Near-term work includes RSS/Atom, a public roadmap, and continued work on "
        "observability, performance, and content quality.",
        "siteBuild.next.articlesLink": "Go to articles",
    },
}
