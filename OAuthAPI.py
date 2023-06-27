import requests
import urllib3

from Utils.Configurations import *

# Verify = False is used to handle ssl certificates things
# urllib3.disable_warnings() disabling warnings
# at correct password it will give status code
config = getConfig()
url = config['API']['github_endpoint']

urllib3.disable_warnings()
username = getUsername()
token = getAccessToken()
response = requests.get(url, verify=False, auth=(username, token))
print(response.json())
print(response.status_code)
