from behave import *

@given(u'I login application')
def step_impl(context):
    print("login app")
    #raise NotImplementedError(u'STEP: Given I login application')

@when(u'I click User icon 2')
def step_impl(context):
    print("user icon")
    #raise NotImplementedError(u'STEP: When I click User icon')

@then(u'I see My profile')
def step_impl(context):
    print("Profile")
    #raise NotImplementedError(u'STEP: Then I see My profile')

@given(u'I selec change pic')
def step_impl(context):
    print("Pic")
 #   raise NotImplementedError(u'STEP: Given I selec change pic')

@when(u'I select a new image from my PC')
def step_impl(context):
    pass
    #$raise NotImplementedError(u'STEP: When I select a new image from my PC')

@then(u'I see new picture loaded')
def step_impl(context):
    print("pic l:")
    #raise NotImplementedError(u'STEP: Then I see new picture loaded')

@given(u'I selec change pass')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Given I selec change pass')


@then(u'I should see confirmation message')
def step_impl(context):
    pass
    #raise NotImplementedError(u'STEP: Then I should see confirmation message')
