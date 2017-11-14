from compare import *

@given(u'I have ${my_balance} in my account')
def step_impl(context, my_balance):
    context.balance = int(my_balance)

@when(u'I choose withdraw the fixed amount of ${my_desired_withdraw}')
def step_impl(context, my_desired_withdraw):
    context.withdraw = int(my_desired_withdraw)

@then(u'I should receive ${cash} cash')
def step_impl(context, cash):
    print("This is your cash $",cash)


@then(u'the balance of my account should be ${remaining_cash}')
def step_impl(context, remaining_cash):
    remainig = context.balance - context.withdraw
    expect(remainig) == int(remaining_cash)