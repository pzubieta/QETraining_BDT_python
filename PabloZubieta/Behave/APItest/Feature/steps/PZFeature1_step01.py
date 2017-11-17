from behave import given

@given(u'I have ${amount:d} in my Account')
def step_impl(context, amount):
    raise NotImplementedError(u'STEP: Given I have $100 in my Account')