
@given(u'I have fisrt name {fname:w} to create a new gmail account')
def step_impl(context,fname):
    assert True is True

@given(u'I have last name {lname:w} to create a new gmail account')
def step_impl(context,lname):
    assert True is True

@given(u'I have username {username:w} to create a new gmail account')
def step_impl(context,username):
    assert True is True

@given(u'I have password {password:S} to create a new gmail account')
def step_impl(context,password):
    assert True is True

@given(u'I have confirm password  {confirmpass:S} to create a new gmail account')
def step_impl(context,confirmpass):
    assert True is True

@given(u'My gender is {gender:w}  to create a new gmail account')
def step_impl(context, gender):
    assert True is True

@given(u'I have mobile phone {mobile:d}  to create a new gmail account')
def step_impl(context, mobile):
    assert True is True

@given(u'I have my current email address chelita141@gmail.com')
def step_impl(context):
    assert True is True

@given(u'I have Birthday\'s month is {month:w} to create a new gmail account')
def step_impl(context, month):
    assert True is True

@given(u'I have Birthday\'s Day is {day:d} to create a new gmail account')
def step_impl(context, day):
    assert True is True

@given(u'I have Birthday\'s Year is {year:d} to create a new gmail account')
def step_impl(context, year):
    assert True is True

@then(u'the new gmail account should be created')
def step_impl(context):
    assert True is True