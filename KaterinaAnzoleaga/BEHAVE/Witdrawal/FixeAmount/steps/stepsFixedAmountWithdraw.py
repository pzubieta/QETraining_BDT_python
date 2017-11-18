from compare import expect

@given(u'I have ${balance:n} in my account')
def step_impl(context, balance):
    context.balance = int(balance)

@when(u'I choose to withdraw the fixes amount of ${withdrawalAmount:n}')
def step_impl(context, withdrawalAmount):
    context.wihdraw=int(withdrawalAmount)

@then(u'I shoudl receive ${cash:n} cash')
def step_impl(context, cash):
    print ("This is your $:", cash)


@then(u'the balance of my account should be ${newBalance:n}')
def step_impl(context, newBalance):
    remaining = context.balance-context.wihdraw
    expect(remaining).to_equal(int(newBalance))
