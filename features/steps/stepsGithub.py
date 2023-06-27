from behave import *
import requests
import urllib3

from Utils.Configurations import *


@given(u'I have a github auth credentials')
def step_impl(context):
    config = getConfig()
    context.url = config['API']['github_endpoint']
    context.username = getUsername()
    context.token = getAccessToken()
    urllib3.disable_warnings()


@when(u'I hit getRepo API of github')
def step_impl(context):
    context.response = requests.get(context.url, verify=False, auth=(context.username, context.token))


@then(u'status code of response should be {statuscode:d}')
def step_impl(context, statuscode):
    print(context.response.status_code)
    assert context.response.status_code == statuscode
