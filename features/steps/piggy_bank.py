from behave import given
from behave import then
from behave import when
from dependency_injector import providers

from infrastructure.adapters.memory.memory_piggy_bank_persistence import MemoryPiggyBankPersistence
from infrastructure.adapters.rest.main import app


@given(u'储蓄罐里现在有{amount}元')
def step_impl(context, amount):
    app.container.piggy_bank_repository.override(providers.Singleton(MemoryPiggyBankPersistence, balance=float(amount)))
    app.container.piggy_bank_service.reset()


@when(u'我查看储蓄罐余额')
def step_impl(context):
    pass


@when(u'我往储蓄罐里存入{amount}元钱')
def step_impl(context, amount):
    context.client.post("/piggy-bank/deposit", json={"amount": float(amount)})


@then(u'储蓄罐余额是{amount}元')
def step_impl(context, amount):
    response = context.client.get("/piggy-bank/balance")
    balance = response.json().get("balance")
    assert balance == float(amount)
