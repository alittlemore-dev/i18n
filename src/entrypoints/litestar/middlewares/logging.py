import uuid

import structlog.contextvars
from litestar.middleware import ASGIMiddleware
from litestar.types import ASGIApp, Receive, Scope, Send


class RequestIdLoggingMiddleware(ASGIMiddleware):
    async def handle(self, scope: Scope, receive: Receive, send: Send, next_app: ASGIApp) -> None:
        tokens = structlog.contextvars.bind_contextvars(request_id=str(uuid.uuid4()))
        try:
            await next_app(scope, receive, send)
        finally:
            structlog.contextvars.reset_contextvars(**tokens)
