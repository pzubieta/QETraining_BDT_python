@given(u'Person ZipCode: {zip:d}')
def step_impl(context,zip):
    a=zip


@given(u'Person Country is : {country:w}')
def step_impl(context,country):
    b=country


@given(u'Num habitants is : {number:n}')
def step_impl(context,number):
    c=number


