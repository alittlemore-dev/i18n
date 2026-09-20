from dishka import FromDishka
from dishka.integrations.litestar import DishkaRouter
from litestar import Controller, Response, get

from infra.healthcheck import ReadinessChecker


class HealthcheckController(Controller):
    path = "/healthcheck"

    @get("", cache=False)
    async def health(self) -> Response[str]:
        return Response(content="", status_code=200)

    @get("/ready", cache=False)
    async def ready(self, checker: FromDishka[ReadinessChecker]) -> Response[str]:
        await checker.check()
        return Response(content="", status_code=200)


api_router = DishkaRouter(
    "",
    route_handlers=[HealthcheckController],
    include_in_schema=False,
    opt={"auth_public": True},
)
