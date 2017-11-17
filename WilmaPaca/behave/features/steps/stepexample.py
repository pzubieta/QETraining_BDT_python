
@given(u'I have ${amount} in my Account')
def step_impl(context,account):
    raise NotImplementedError(u'STEP: Given I have ${amount} in my Account')

@when(u'I request ${amount} of my account')
def step_impl(context,amount1):
    pass
    #raise NotImplementedError(u'STEP: When I request ${amount} of my account')

@then(u'My account is {amount} substraction {amount1}')
def step_impl(context,num,num2):
    raise NotImplementedError(u'STEP: Then My account is {amount} substraction {amount1}')

@then(u'I have happy')
def step_impl(context):
    pass