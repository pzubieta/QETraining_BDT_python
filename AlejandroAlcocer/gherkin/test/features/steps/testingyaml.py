from compare import expect

@given('I have connection to "{host}"')
def step_impl(context, host):
    expect(context.host).to_equal(host)

@when('I send {method}')
def step_impl(context, method):
    expect(context.method).to_equal(method)

@then('I receive status code {code}')
def step_impl(context, code):
    expect(str(context.code)).to_equal(code)
