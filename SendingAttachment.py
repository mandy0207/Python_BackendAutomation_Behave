import requests

url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open(r'C:\Users\msingh\Desktop\API Learning\krishna.jpg', 'rb')}
response = requests.post(url, files=files)
print(response.status_code)
print(response.json())
