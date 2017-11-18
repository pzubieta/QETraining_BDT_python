from utils.utils import *
from compare import expect


@when('I need to test the response in the {method} method with {snippet}')
def step_impl(context, method, snippet):
    context.method = method
    context.payload = {"part": snippet, "key": context.apiKey}

@then('I get a {code:d} response')
def step_impl(context, code):
    context.code = code
    expect(context.code).to_equal(get_conn(context.host, context.rootpath,
                                           context.method, context.payload))
