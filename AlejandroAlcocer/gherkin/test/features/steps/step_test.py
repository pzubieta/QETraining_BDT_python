from behave import given, when, then
from compare import expect, to_equal

@given('I fill the zip code field with {zip_code:d}')
def step_impl(context, zip_code):
    print(zip_code)

@given('I fill the country field with {country:w}')
def step_impl(context, country):
    print(country)

@given('I fill the number with thousands with {people:f}')
def step_impl(context, people):
    print(people)
