from typing import Any

from litestar.openapi import ResponseSpec
from litestar.openapi.spec import Example
from verbose_http_exceptions import InternalServerErrorHTTPException
from verbose_http_exceptions.exc.base import VerboseHTTPExceptionDict
from verbose_http_exceptions.ext.litestar.exc import ValidationHTTPException


class JSONExample(Example):
    def to_schema(self) -> dict[str, Any]:
        result = super().to_schema()
        # Litestar otherwise drops required nullable fields from dictionary examples.
        if self.value is not None:
            result["value"] = self.value
        return result


def error_responses(*, validation: bool = False) -> dict[int, ResponseSpec]:
    responses = {
        500: ResponseSpec(
            data_container=VerboseHTTPExceptionDict,
            description="Unexpected service failure. Internal details are not exposed.",
            generate_examples=False,
            examples=[JSONExample(value=InternalServerErrorHTTPException().as_dict())],
        ),
    }
    if validation:
        responses[400] = ResponseSpec(
            data_container=VerboseHTTPExceptionDict,
            description=(
                "Unsupported bundle or language. The error uses code, type, message, "
                "location and attr; multiple failures include recursive nested_errors. "
                "location and attr may be null. Error keys use snake_case."
            ),
            generate_examples=False,
            examples=[
                JSONExample(
                    summary="Unsupported language in the request path",
                    value=ValidationHTTPException(
                        message="Input should be 'ru' or 'en'",
                        location="path",
                        attr_name="language",
                        type_="enum",
                    ).as_dict(),
                ),
            ],
        )
    return responses
