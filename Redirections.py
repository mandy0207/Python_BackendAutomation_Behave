import requests

url = "https://rahulshettyacademy.com/"

cookie = {'visit-month': 'March'}
response = requests.get(url, allow_redirects=False, cookies=cookie, timeout=2)
# print(response.history)
print(response.status_code)
