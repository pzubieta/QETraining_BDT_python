
@given(u'I have ${balance} in my Account')
def step_impl(context, balance):
    #raise NotImplementedError(u'STEP: Given I have $100 in my Account')
    return balance-20


@when(u'I enter 20 as the withdrawal amount')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter 20 as the withdrawal amount')


@when(u'Confirm withdrawal')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Confirm withdrawal')

@then(u'My new balance will be 100 - 20')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then My new balance will be 100 - 20')
