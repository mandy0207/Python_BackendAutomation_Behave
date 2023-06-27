import requests
import urllib3

from Utils.Configurations import *

# Verify = False is used to handle ssl certificates things
# urllib3.disable_warnings() disabling warnings
# at correct password it will give status code
config = getConfig()
url = config['API']['github_endpoint']
username = getUsername()
token = getAccessToken()
urllib3.disable_warnings()
response = requests.get(url, verify=False, auth=(username, token))
print(response.status_code)

# Api to see list of repositories when there is username and password associated to any api we can create a session
# of that credentials and can use across all api requests

# session created below

se = requests.session()
se.auth = auth = (username, token)

url2 = config['API']['github_repo_endpoint']

# we can make below request with se object
response = se.get(url2, verify=False, )

print(response.json())
print(response.status_code)
