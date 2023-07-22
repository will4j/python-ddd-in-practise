from behave import given
from behave import then
from behave import when


@given(u'储蓄罐里现在有{amount}元')
def step_impl(context, amount):
    raise NotImplementedError(u'STEP: Given 储蓄罐里现在有5元')


@when(u'我查看储蓄罐余额')
def step_impl(context):
    raise NotImplementedError(u'STEP: When 我查看储蓄罐余额')


@when(u'我往储蓄罐里存入{amount}元钱')
def step_impl(context, amount):
    raise NotImplementedError(u'STEP: When 我往储蓄罐里存入1元钱')


@then(u'储蓄罐余额是{amount}元')
def step_impl(context, amount):
    raise NotImplementedError(u'STEP: Then 储蓄罐余额是5元')
