import asyncio

from fastapi import FastAPI
from hypercorn.asyncio import serve
from hypercorn.config import Config
from infrastructure.factory.di.piggy_bank_container import PiggyBankContainer

from infrastructure.adapters.rest.endpoints import piggy_bank_endpoints

app = FastAPI()
app.container = PiggyBankContainer()

app.include_router(piggy_bank_endpoints.router)

if __name__ == '__main__':
    asyncio.run(serve(app, Config()))
