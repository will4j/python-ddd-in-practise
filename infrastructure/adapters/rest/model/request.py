from pydantic import BaseModel


class DepositRequest(BaseModel):
    amount: float
