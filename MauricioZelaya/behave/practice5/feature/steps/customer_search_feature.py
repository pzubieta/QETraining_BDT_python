from compare import *


@given(u'a {customer_id:d}')
def step_impl(context, customer_id):
    context.customer_id = customer_id


@given(u'a {customer_name:w}')
def step_impl(context, customer_name):
    context.customer_name = customer_name


@when(u'I request the {total_amount:d} of a purchase')
def step_impl(context, total_amount):
    context.total_amount = total_amount


@then(u'I get the {customer_id:d}')
def step_impl(context, customer_id):
    expect(context.customer_id).to_equal(customer_id)


@then(u'I get the {customer_name:w}')
def step_impl(context, customer_name):
    if customer_name in context.users.values():
        expect(context.customer_name).to_equal(context.users[context.customer_id])






