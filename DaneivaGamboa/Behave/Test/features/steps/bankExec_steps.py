from behave import then, when, given
from compare import expect


@given(u'I have ${amount:d} in my account')
def step_impl(context,amount):
    context.amount = int(amount)

    ## raise NotImplementedError(u'STEP: Given I have $500 in my account')

@when(u'I choose to withdraw the fixed amount of ${fixed_amount:d}')
def step_impl(context,fixed_amount):
    context.fixed_amount= int(fixed_amount)

   ## raise NotImplementedError(u'STEP: When I choose to withdraw the fixed amount of $50')

@then(u'I should receive ${fixed_amount:d} cash')
def step_impl(context,fixed_amount):
    print("this is your cash:", fixed_amount )
    ##raise NotImplementedError(u'STEP: Then I should receive $50 cash')

@then(u'the balance of my account should be ${balance}')
def step_impl(context,balance):
    remaining= context.amount-context.fixed_amount
    expect(remaining).to_equal(int(balance))
    ## raise NotImplementedError(u'STEP: Then the balance of my account should be $450')

