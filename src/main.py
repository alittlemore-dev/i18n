from litestar import Litestar

from entrypoints.litestar.initializers.main import create_litestar_app
from infra.ioc.container import create_container


def create_app() -> Litestar:
    return create_litestar_app(container=create_container())
