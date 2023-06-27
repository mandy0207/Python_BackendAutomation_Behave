import requests
from behave import *
from Payload import *
from Utils.Configurations import *
from Utils.APIResources import *


@given(u'the book details which need to be added to Library')
def step_impl(context):
    config = getConfig()
    context.AddBook_Url = config['API']['endpoint'] + APIResources.addBook
    context.DelBook_Url = config['API']['endpoint'] + APIResources.delBook


@when(u'we execute AddBook PostAPI method')
def step_impl(context):
    addBook_response = requests.post(context.AddBook_Url, json=addbook_Paylod(), headers=addbook_requestHeaders())
    context.addBook_response_json = addBook_response.json()


@then(u'book is successfully added')
def step_impl(context):
    print(context.addBook_response_json)
    context.Book_id = context.addBook_response_json['ID']
    print(context.Book_id)
    assert context.addBook_response_json['Msg'] == "successfully added"


@when(u'we execute AddBook PostAPI method with {name} {aisle} {author}')
def step_impl(context, name, aisle, author):
    print("Executed Data=", name, aisle, author)
    addBook_response = requests.post(context.AddBook_Url, json=addbook_Paylod_Example(name, aisle, author), headers=addbook_requestHeaders())
    context.addBook_response_json = addBook_response.json()

