#@given(u'I have $100 in my Account')
#def step_impl(context):
	#pass
#	raise NotImplementedError(u'STEP: Given I have $100 in my Account')
	
#@given(u'I have $250 in my Account')
#def step_impl(context):
	#pass
    #raise NotImplementedError(u'STEP: Given I have $250 in my Account')

@given(u'I have ${amount:d} in my Account')
def step_impl(context, amount):
	assert True is True
	#raise NotImplementedError(u'STEP: Given I have ${amount} in my Account')

@given(u'zipCode is {zip:d}')
def step_impl(context, zip):
    assert True is True
	#raise NotImplementedError(u'STEP: Given zipCode is ${zip}')

@given(u'Country is "{country:w}"')
def step_impl(context, country ):
    assert True is True
	#raise NotImplementedError(u'STEP: Given Country is ${country}')

@given(u'Nro Habitants is "{habitants:n}"')
def step_impl(context, habitants):
    assert True is True
	#raise NotImplementedError(u'STEP: Given Nro Habitants is ${habitants}')