from utils.utils import *
from compare import expect


@given(u'{vID} video id for a comment thread')
def step_impl(context, vID):
    context.videoID = vID


@when(u'I send a {method} comment threads list using {service}')
def step_impl(context, method, service):
    context.method = method
    context.service = service


@then(u'status code {code} is received')
def step_impl(context, code):
    payload = {"key": context.apiKey, "videoId": context.videoID, "part": "snippet"}
    currentStatusCode = get_conn(context.host, context.rootpath, context.service, context.method, payload)
    expect(currentStatusCode).to_equal(int(code))


