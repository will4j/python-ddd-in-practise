from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import APIRouter
from fastapi import Depends

from application.piggy_bank_service import PiggyBankServie
from infrastructure.adapters.rest.model.request import DepositRequest
from infrastructure.adapters.rest.model.response import CheckBalanceResponse
from infrastructure.adapters.rest.model.response import DepositResponse
from infrastructure.factory.di.piggy_bank_container import PiggyBankContainer

router = APIRouter(prefix="/piggy-bank")


@router.get('/balance', response_model=CheckBalanceResponse)
@inject
async def check_balance(piggy_bank_service: PiggyBankServie = Depends(Provide[PiggyBankContainer.piggy_bank_service])):
    balance = piggy_bank_service.balance()
    return {
        "balance": balance
    }


@router.post('/deposit', response_model=DepositResponse)
@inject
async def check_balance(request: DepositRequest,
                        piggy_bank_service: PiggyBankServie = Depends(Provide[PiggyBankContainer.piggy_bank_service])):
    piggy_bank_service.deposit(request.amount)
    return {
        "success": True
    }
