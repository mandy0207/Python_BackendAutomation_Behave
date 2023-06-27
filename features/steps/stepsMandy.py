import requests
from behave import *
from Payload import *
from Utils.Configurations import *
from Utils.APIResources import *


@given(u'when we are aware with the name of coder')
def step_impl(context):
    print("I am in given")


@when(u'the coder name is printed')
def step_impl(context):
    print("I am in when")


@when(u'the coder name is printed again')
def step_impl(context):
    for row in context.table:
        # print(row)
        # print(type(row))
        firstname = row["firstname"]
        lastname = row["lastname"]
        print("My name is", firstname, lastname)



@then(u'Hello Hello Hello')
def step_impl(context):
    print("Hello Hello Hello")


@then(u'the name is concatenated with {name}')
def step_impl(context, name):
    print("I am in then", name)


@then(u'the name is concatenated {name} {age}')
def step_impl(context, name, age):
    print("I am ", name, "My age is =", age)
