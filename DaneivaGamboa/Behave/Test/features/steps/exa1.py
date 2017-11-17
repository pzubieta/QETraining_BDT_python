from behave import then, when


@when(u'I select "asd')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select "asd')

@then(u'My result should be "a"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then My result should be "a"')


