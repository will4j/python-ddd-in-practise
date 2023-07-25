import asyncio

from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config

from infrastructure.adapters.rest.endpoints import piggy_bank_endpoints
from infrastructure.factory.di.piggy_bank_container import PiggyBankContainer


def create_app() -> FastAPI:
    container = PiggyBankContainer()

    app = FastAPI()
    app.container = container
    app.include_router(piggy_bank_endpoints.router)
    return app


app = create_app()

if __name__ == '__main__':
    asyncio.run(serve(app, Config()))
