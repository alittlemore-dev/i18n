import hashlib
import json
from dataclasses import dataclass

from litestar import Request

from core.i18n.catalogs import CATALOGS
from core.i18n.enums import LanguageEnum


@dataclass(frozen=True)
class I18nCacheKey:
    revision: str
    default_language: LanguageEnum

    def __call__(self, request: Request) -> str:
        return f"i18n:{self.revision}:{self.default_language}:{request.url.path}"


def create_i18n_cache_key(default_language: LanguageEnum) -> I18nCacheKey:
    content = json.dumps(CATALOGS, ensure_ascii=False, sort_keys=True).encode()
    return I18nCacheKey(hashlib.sha256(content).hexdigest(), default_language)
