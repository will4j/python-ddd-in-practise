import asyncio

from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config

from infrastructure.adapters.rest.endpoints import piggy_bank_endpoints
from infrastructure.factory.di.piggy_bank_container import PiggyBankContainer


def create_app(container=PiggyBankContainer()) -> FastAPI:
    app = FastAPI()
    app.container = container
    app.include_router(piggy_bank_endpoints.router)
    return app


def run(app=create_app(), bind="127.0.0.1:8000"):
    app_config = Config()
    app_config.bind = bind

    asyncio.run(serve(app, app_config))  # type: ignore


if __name__ == '__main__':
    run()
