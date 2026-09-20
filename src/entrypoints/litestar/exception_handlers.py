from typing import Any

from litestar import Request, Response
from verbose_http_exceptions import InternalServerErrorHTTPException
from verbose_http_exceptions.exc.base import VerboseHTTPExceptionDict
from verbose_http_exceptions.ext.litestar import (
    ALL_EXCEPTION_HANDLERS_MAP,
    verbose_http_exception_handler,
)
from verbose_http_exceptions.ext.litestar.types import LitestarExceptionHandlersMap

from infra.healthcheck import ReadinessCheckError


def unexpected_exception_handler(
    request: Request[Any, Any, Any],
    _exc: Exception,
) -> Response[VerboseHTTPExceptionDict]:
    return verbose_http_exception_handler(
        request,
        InternalServerErrorHTTPException(message=InternalServerErrorHTTPException.message),
    )


def readiness_check_error_handler(
    _request: Request[Any, Any, Any],
    _exc: Exception,
) -> Response[str]:
    return Response(content="", status_code=503)


def get_litestar_exception_handlers() -> LitestarExceptionHandlersMap:
    return {
        **ALL_EXCEPTION_HANDLERS_MAP,
        Exception: unexpected_exception_handler,
        ReadinessCheckError: readiness_check_error_handler,
    }
