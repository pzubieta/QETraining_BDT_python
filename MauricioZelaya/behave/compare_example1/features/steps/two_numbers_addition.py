from steps.calculations import *

@given(u'I have {num_1:d} and {num_2:d}')
def step_impl(context, num_1, num_2):
    context.num_1 = num_1
    context.num_2 = num_2
    # raise NotImplementedError(u'STEP: Given I have 2 and 2')

@when(u'I select sum')
def step_impl(context):
    print("we will sum two numbers")


@then(u'My result should be 4')
def step_impl(context):
    add = addition(context.num_1, context.num_2)

