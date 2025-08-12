from aiogram import Router
from .handlers import start_router, code_router, encode_router


def get_routers() -> Router:
    router = Router()
    router.include_router(start_router)
    router.include_router(code_router)
    router.include_router(encode_router)
    return router
