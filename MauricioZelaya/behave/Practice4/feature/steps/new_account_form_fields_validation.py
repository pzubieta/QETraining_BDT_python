@given(u'user first name is {first_name:w}')
def step_impl(context, first_name):
    raise NotImplementedError(u'STEP: Given user first name is Mauricio')

@given(u'user last name is {last_name:w}')
def step_impl(context, last_name):
    raise NotImplementedError(u'STEP: Given user last name is Zelaya')

@given(u'desired username is {user_name:w}')
def step_impl(context, user_name):
    raise NotImplementedError(u'STEP: Given desired username is maurizel')

@given(u'password is {password}')
def step_impl(context, password):
    raise NotImplementedError(u'STEP: Given password is Control1234_')

@given(u'confirm password contains {confirm_password}')
def step_impl(context, confirm_password):
    raise NotImplementedError(u'STEP: Given confirm password contains Control1234_')

@given(u'birthday month is {birth_month:d}')
def step_impl(context, birth_month):
    raise NotImplementedError(u'STEP: Given birthday month is 3')

@given(u'birthday day is {birth_day:d}')
def step_impl(context, birth_day):
    raise NotImplementedError(u'STEP: Given birthday day is 11')

@given(u'birthday year is {birth_year:d}')
def step_impl(context, birth_year):
    raise NotImplementedError(u'STEP: Given birthday year is 1980')

@given(u'Mobile phone is {phone_number:d}')
def step_impl(context, phone_number):
    raise NotImplementedError(u'STEP: Given Mobile phone is 70720612')

@given(u'has not current email address')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given has not current email address')
