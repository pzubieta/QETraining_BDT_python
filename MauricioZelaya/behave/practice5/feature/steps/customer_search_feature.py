# from steps.dataCollections import *
from compare import *

@given(u'a {customer_id:d}')
def step_impl(context, customer_id):
    context.customer_id = customer_id

@when(u'I request the {total_amount:d} of a purchase')
def step_impl(context, total_amount):
    context.total_amount = total_amount

@then(u'I get the {customer_id:d} information')
def step_impl(context, customer_id):
    expect(context.customer_id).to_equal(int(customer_id))




