
@given(u'I want to fill the name {name:w}')
def step_impl(context, name):
    print(name)

@given(u'I want to fill the last name {last_name_1:w} {last_name_2:w}')
def step_impl(context, last_name_1, last_name_2):
    print(last_name_1 + last_name_2)

@given(u'I want to fill the username {username:w}')
def step_impl(context, username):
    print(username)

@given(u'I want to create a password {password:w}')
def step_impl(context, password):
    print(password)

@given(u'I want to confirm my password {password:w}')
def step_impl(context, password):
    print(password)

@given(u'I want to set a month for my birthday {month:S}')
def step_impl(context, month):
    print(month)

@given(u'I want to set a day for my birthday {day:d}')
def step_impl(context, day):
    print(day)

@given(u'I want to set a year for my birthday {year:d}')
def step_impl(context, year):
    print(year)

@given(u'I want to select my gender {gender:S}')
def step_impl(context, gender):
    print(gender)

@given(u'I want to set my country {country:S}')
def step_impl(context, country):
    print(country)

@given(u'I want to insert my phone number {phone:d}')
def step_impl(context, phone):
    print(phone)

@given(u'I want to set my current email {email:w}')
def step_impl(context, email):
    print(email)
