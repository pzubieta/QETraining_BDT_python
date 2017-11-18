
@given(u'I have ZipCode {ZipCode:d}')
def step_impl(context,ZipCode):
    w=ZipCode

@given(u'The country is {Country:w}')
def step_impl(context,Country):
    w = Country

@given(u'I got habitant number: {nhab:n}')
def step_impl(context,nhab):
    w = nhab