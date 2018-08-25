# importing the requests library
import requests
import json
from pprint import pprint

# defining the API parameters
# read spark token from file 'sparkToken'
with open('sparkToken') as token:
    API_TOKEN = token.read()
API_ENDPOINT = "https://api.ciscospark.com/v1/people"
API_KEY_ROOT = 'Bearer '
API_KEY = API_KEY_ROOT + API_TOKEN

headers = {
    'Authorization': API_KEY,
}

response = requests.get(API_ENDPOINT, headers=headers)

# extracting response text
str_response = response.text

# use the json module to parse the JSON string into native Python data
json_data = json.loads(str_response)

# display the JSON response
pprint(json_data)

# save data as JSON
with open('result.json', 'w') as f:
    json.dump(str_response, f)
    print("Scrittura JSON")
