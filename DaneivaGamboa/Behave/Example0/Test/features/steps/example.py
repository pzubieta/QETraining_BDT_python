from behave import given


@given(u'I have a ${amount:d} in my account')
def step_impl(context, amount):
    print("PASSED test")
    # raise NotImplementedError(u'STEP: Given I have a 100$ in my account')



