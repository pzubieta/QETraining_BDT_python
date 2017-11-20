from behave import given

@given(u'an authenticated user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given an authenticated user')

@when(u'I send a GET playlist')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I send a GET playlist')

@given(u'I as an authenticated user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I as an authenticated user')

@when(u'I send a TestPlaylist1')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I send a TestPlaylist1')

@when(u'I send a This is a PL1')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I send a This is a PL1')

@when(u'I send a TestPlaylist2')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I send a TestPlaylist2')

@when(u'I send a This is a PL2')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I send a This is a PL2')

@when(u'I send a new newTitle')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I send a new newTitle')

@when(u'I send a new newDescription')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I send a new newDescription')

@then(u'I get a response with the playlist with newTitle as title')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get a response with the playlist with newTitle as title')

@then(u'newDescription as description')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then newDescription as description')

@when(u'I send the ID of a playlist to be Delete')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I send the ID of a playlist to be Delete')

@then(u'I get a response with the playlist resource')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get a response with the playlist resource')


