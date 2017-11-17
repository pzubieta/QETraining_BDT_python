@given(u'I have ${amount:d}')
def step_impl(context,amount):
    a=amount
#@given(u'I have $250')
#def step_impl(context):
#   a=250

@when(u'I worked and I recieved my salary')
def step_impl(context):
     context.b=15+content.a

@then(u'I should optain money by bank')
def step_impl(context):
   c=1+context.b
