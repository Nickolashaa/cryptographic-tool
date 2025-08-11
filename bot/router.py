from aiogram import Router
from .handlers import start_router


def get_routers() -> Router:
    router = Router()
    router.include_router(start_router)
    return router
