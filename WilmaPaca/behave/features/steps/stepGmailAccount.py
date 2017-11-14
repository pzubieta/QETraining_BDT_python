@given(u'I want to create an gmail account in: \'www.gmail.com\'')
def step_impl(context):
    url = "www.gmail.com"

@given(u'I want to create an gmail account in: {url:w}')
def step_impl(context,url):
    url_endpoint = url

@given(u'My name is: {name:w} {lastname:w}')
def step_impl(context,name,lastName):
    name_u =name
    last_u =lastName

@given(u'username: {userame:w}')
def step_impl(context,username):
    username_u = username+"@gmail.com"

@given(u'password: {password}')
def step_impl(context,password):
    password_u = password

@given(u'Cofirm to password: {password}')
def step_impl(context,password):
    confirm_pass = password

@given(u'Birthday: {day:d} {month:w} {year:d}')
def step_impl(context, day,month, year):
    day_b = day
    month_b = month
    year_b = year

@given(u'Gender: {gender:w}')
def step_impl(context,gender):
    gender_u = gender

@given(u'Mobile phone: {phone:d}')
def step_impl(context,phone):
    num_phone = phone

@given(u'My current email: \'florpaty@gmail.com\'')
def step_impl(context):
    w=1

@given(u'My current email: {email:w}')
def step_impl(context,email):
    email_c = email

@then(u'I have a new email')
def step_impl(context):
    pass