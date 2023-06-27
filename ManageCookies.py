import requests

url = "https://rahulshettyacademy.com/"

cookie = {'visit-month': 'March'}
response = requests.get(url, cookies=cookie)
print(response.status_code)

# it returns cookie which ever is sent

url2 = "https://httpbin.org/cookies"
response = requests.get(url2, cookies=cookie)
print(response.status_code)
response_json = response.json()
print(response_json)
