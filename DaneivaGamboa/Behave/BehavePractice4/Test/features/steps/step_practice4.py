from behave import given


@given(u'I enter the Zipcode {zipcode:d}')
def step_impl(context, zipcode):

    raise NotImplementedError(u'STEP: Given I enter the Zipcode {}'.format(zipcode))

@given(u'I enter country {country:w}')
def step_impl(context,country):
    raise NotImplementedError(u'STEP: Given I enter country %s',country)

@given(u'I enter nro_habitats {nro_habitats:n}')
def step_impl(context, nro_habitats):
    raise NotImplementedError(u'STEP: Given I enter nro_habitats %d',nro_habitats)
