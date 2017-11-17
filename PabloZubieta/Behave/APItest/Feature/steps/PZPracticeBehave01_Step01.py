@given(u'I have the zipcode {zipcode:d}')

def step_impl(context,zipcode):
    raise NotImplementedError(u'STEP: Given I have the zipcode 1234')

@given(u'I have set the country {country}')
def step_impl(context,country):
    assert True is True
    '''raise NotImplementedError(u'STEP: Given I have set the country {country}')'''

@given(u'I set the number of inhabitants {inhabitants:n}')
def step_impl(context,inhabitants):
    raise NotImplementedError(u'STEP: Given I set the number of inhabitants {inhabitants:n}')
