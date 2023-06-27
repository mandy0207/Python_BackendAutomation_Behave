from behave import *

from pageObjects.CheckWrappersPage import *


@given(u'user logins')
def step_impl(context):
    cp = CheckWrapperPage(context.driver)
    cp.AllOperations()


@when(u'user perform testing')
def step_impl(context):
    print("I am in when")


@then(u'user perform validation')
def step_impl(context):
    print("I am in when")
