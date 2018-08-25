# importing the requests library
import requests
import json
from pprint import pprint

class postOnRoom():

    def __init__(self):

        # defining the API parameters
        # read spark token from file 'sparkToken'
        with open('sparkToken') as self.token:
            self.API_TOKEN = self.token.read()

        self.API_ENDPOINT = "https://api.ciscospark.com/v1/messages"
        self.API_KEY_ROOT = 'Bearer '
        self.API_KEY = self.API_KEY_ROOT + self.API_TOKEN
        self.HEADERS = {
            'Authorization': self.API_KEY,
        }


    def send(self, recipient, message):

        data = [
          ('toPersonEmail', recipient),
          ('text', message),
        ]

        # send message
        response = requests.post(self.API_ENDPOINT, headers=self.HEADERS, data=data)

        # extracting response text
        str_response = response.text

        # use the json module to parse the JSON string into native Python data
        json_data = json.loads(str_response)

        # display the JSON response
        pprint(json_data)
