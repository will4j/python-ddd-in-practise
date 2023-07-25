from pydantic import BaseModel


class CheckBalanceResponse(BaseModel):
    balance: float


class DepositResponse(BaseModel):
    success: bool
