import random
import time

import requests

from Payload import *
from Utils.Configurations import *
from Utils.APIResources import *

config = getConfig()
AddBook_Url = config['API']['endpoint'] + APIResources.addBook
DelBook_Url = config['API']['endpoint']+APIResources.delBook

query = 'Select * from Books'
addBook_response = requests.post(AddBook_Url, json=buildPayloadFromDB(query), headers=addbook_requestHeaders())
addBook_response_json = addBook_response.json()
print(addBook_response_json)
assert addBook_response_json['Msg'] == "successfully added"
assert addBook_response.status_code == 200

Book_id = addBook_response_json['ID']
print(Book_id)

delete_data = {
    "ID": Book_id
}

DelBook_response = requests.post(DelBook_Url, json=delete_data, headers=addbook_requestHeaders())
del_response_json = DelBook_response.json()
print(del_response_json)
assert del_response_json['msg'] == 'book is successfully deleted'
assert DelBook_response.status_code == 200



