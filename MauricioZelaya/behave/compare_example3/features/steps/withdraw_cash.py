from compare import *
from steps.utils import reduce_balance

@given(u'I have ${current_amount_into_account:d} in my account')
def step_impl(context, current_amount_into_account):
    context.balance = int(current_amount_into_account)

@when(u'I choose withdraw the fixed amount of ${amount_to_withdraw:d}')
def step_impl(context, amount_to_withdraw):
    context.withdraw = int(amount_to_withdraw)

@then(u'I should receive ${amount_received:d} cash')
def step_impl(context, amount_received):
    print("please get your money %s" % amount_received)

@then(u'the balance of my account should be ${current_amount_into_account:d}')
def step_impl(context, current_amount_into_account):
    remaining = reduce_balance(context.balance, context.withdraw)
    expect(remaining).to_equal(int(current_amount_into_account))
