from behave import given, when, then
from compare import expect


@given('I have ${amount:f} in my account')
def step_impl(context, amount):
    context.amount = float(amount)



@when('I choose to withdraw the fixed amount of ${amount_to_withdraw:f}')
def step_impl(context, amount_to_withdraw):
    context.amount_to_withdraw = float(amount_to_withdraw)


@then('I should receive ${withdraw:f} cash')
def step_impl(context, withdraw):
    print("here is your {}".format(withdraw))
    expect(context.amount_to_withdraw).to_equal(withdraw)


@then('the balance of my account should be ${balance:f}')
def step_impl(context, balance):
    new_balance = context.amount - context.amount_to_withdraw
    expect(round(new_balance, 2)).to_equal(balance)
