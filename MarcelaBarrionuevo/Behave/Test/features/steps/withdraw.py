from compare import *

@when(u'I choose to withdraw the fixed amount of ${balance:d}')
def step_impl(context, balance):
    context.balance = balance

@then(u'I should receive ${withdraw:d} cash')
def step_impl(context, withdraw):
    context.withdraw = withdraw

@then(u'the balance of my account should be ${cash:d}')
def step_impl(context, cash):
	print ("This is your $",cash)
	
@then(u'the balance of my account should be ${newbalance}')
def step_impl(context, newbalance):
	remaing = context.balance - context.withdraw
	expect(remaing).to_equal(int(newbalance))
	