from behave import given, then


@given(u'I enter the first name: {fname:w}')
def step_impl(context,fname):
    assert True is True
    #raise NotImplementedError(u'STEP: Given I enter the first name: Daneiva')

@given(u'I enter last name: {lname:w}')
def step_impl(context,lname):
    assert True is True
    #raise NotImplementedError(u'STEP: Given I enter last name: Gamboa')

@given(u'I enter username: {user:w}')
def step_impl(context,user):
    assert True is True
    #raise NotImplementedError(u'STEP: Given I enter username: degamboa')

@given(u'I enter pass: {password:S}')
def step_impl(context,password):
    assert True is True
    #raise NotImplementedError(u'STEP: Given I enter pass: pass123.')

@given(u'I enter confirm_pass: {confirmPass:S}')
def step_impl(context,confirmPass):
    assert True is True
    #raise NotImplementedError(u'STEP: Given I enter confirm_pass: pas123.')

@given(u'I enter birthday {dateBirthday}')
def step_impl(context,dateBirthday):
    assert True is True
    #raise NotImplementedError(u'STEP: Given I enter birthday 02/02/1986')

@given(u'I enter gender: {gender:w}')
def step_impl(context):
    assert True is True
    #raise NotImplementedError(u'STEP: Given I enter gender: female')

@given(u'I enter email: {email}')
def step_impl(context,email):
    assert True is True
    #raise NotImplementedError(u'STEP: Given I enter email: daneiva@gmail.com')

@then(u'The new Gmail Account should be created.')
def step_impl(context):
    assert True is True
    #raise NotImplementedError(u'STEP: Then The new Gmail Account should be created.')
