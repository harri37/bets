import requests

class Requester():
    '''Class to handle all requests to varios API's'''

    def __init__(self, url):
        '''
        Creates a new Requester object

            Parameters:
                url (str): Url for api
        '''
        self.url = url

    def makeRequest(self, endpoint = "", headers = None, params = None):
        '''
        Makes a request to the api

            Parameters:
                endpoint (str): endpoint of request
                headers (JSON): request headers
                params (JSON): request parameters

            Returns: 
                response (JSON): response of request
        '''
        response = requests.get(f'{self.url}{endpoint}', headers=headers, params=params)

        if response.status_code != 200:
            print(f'Failed to make request: status_code {response.status_code}, response body {response.text}')
        else:
            return response.json()      
