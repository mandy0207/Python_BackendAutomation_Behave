import json

import requests

response = requests.get("http://216.10.245.166/Library/GetBook.php", params={"AuthorName": "ManinderSingh"}, )


json_response = response.json()
print(type(json_response))
dict = json_response[0]
print(dict["isbn"])

# To check status code
statusCode = response.status_code
print(statusCode)
assert statusCode == 200
print(response.headers)
print(response.headers['Content-Type'])

# Retrieve BookName with isbn = RS217
for data in json_response:
    if data["isbn"] == "RS217":
        print(data)
        for key in data:
            print(key,  '->',  data[key])

expected_data = {
        "book_name": "Learn Ronorex",
        "isbn": "RS217",
        "aisle": "23456"
    }

assert data == expected_data