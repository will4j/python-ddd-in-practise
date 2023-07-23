from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import APIRouter
from pydantic import BaseModel

from application.piggy_bank_service import PiggyBankServie
from infrastructure.factory.di.piggy_bank_container import PiggyBankContainer

router = APIRouter(prefix="/piggy-bank")

piggy_bank_service: PiggyBankServie = Provide[PiggyBankContainer.piggy_bank_service]


class CheckBalanceResponse(BaseModel):
    balance: float


@router.get('/balance', response_model=CheckBalanceResponse)
@inject
async def check_balance():
    balance = piggy_bank_service.balance()
    return {
        "balance": balance
    }


class DepositRequest(BaseModel):
    amount: float


class DepositResponse(BaseModel):
    success: bool


@router.post('/deposit', response_model=DepositResponse)
@inject
async def check_balance(request: DepositRequest):
    piggy_bank_service.deposit(request.amount)
    return {
        "success": True
    }
