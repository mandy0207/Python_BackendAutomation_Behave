import random

from Utils.Configurations import *


def addbook_Paylod():
    random_number = random.randint(1, 100000)
    print(random_number)
    isbn = "{}{}".format("RS", random_number)
    print(isbn)
    data = {

        "name": "Jeet Singh",
        "isbn": isbn,
        "aisle": "23456",
        "author": "Sandy Taak"
    }

    return data


def addbook_Paylod_Example(name, aisle, author):
    random_number = random.randint(1, 100000)
    print(random_number)
    isbn = "{}{}".format("RS", random_number)
    print(isbn)
    data = {

        "name": name,
        "isbn": isbn,
        "aisle": aisle,
        "author": author
    }

    return data


def buildPayloadFromDB(query):
    addBody = {}
    tp = getQuery(query)
    addBody['name'] = tp[0]
    addBody['isbn'] = tp[1]
    addBody['aisle'] = tp[2]
    addBody['author'] = tp[3]
    return addBody


def addbook_requestHeaders():
    req_headers = {
        "Content-Type": "application/json"
    }
