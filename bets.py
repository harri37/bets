import os
import requests

from dotenv import load_dotenv
load_dotenv()

ODDS_API_KEY = os.getenv("ODDS_API_KEY")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")


SPORT = 'upcoming'  # use the sport_key from the /sports endpoint below, or use 'upcoming' to see the next 8 games across all sports

REGIONS = 'au'  # uk | us | eu | au. Multiple can be specified if comma delimited

# h2h | spreads | totals. Multiple can be specified if comma delimited
MARKETS = 'h2h,spreads'

ODDS_FORMAT = 'decimal'  # decimal | american

DATE_FORMAT = 'iso'  # iso | unix
NBA_URL = "https://api-nba-v1.p.rapidapi.com/seasons"

def makeNBARequest(endpoint = "", headers={"X-RapidAPI-Key": RAPID_API_KEY, "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"}):
    '''
    Makes a request to the nba api & print the results

        Paramers:
            endpoint (string): endpoint for api request
            headers (object): Headers for api request

        Returns:
            responseJSON (JSON): Response of request
    '''
    response = requests.get(
        f'{NBA_URL}{endpoint}',
        headers=headers
    )

    if response.status_code != 200:
        print(
            f'Failed to make reques: status_code {response.status_code}, response body {response.text}')

    else:
        responseJSON = response.json()
        print('Results:', responseJSON)
        return responseJSON['response']


def makeOddsRequest(endpoint="", params={'api_key': ODDS_API_KEY}):
    '''
    Makes a request to the odds api & print the results
        Paramers:
            endpoint (string): Endpoint for api request
            params (object): Parameters for api request
        Returns:
            responseJSON (JSON): Response of request
    '''

    response = requests.get(
        f'https://api.the-odds-api.com/v4/sports{endpoint}',
        params
    )

    if response.status_code != 200:
        print(
            f'Failed to make reques: status_code {response.status_code}, response body {response.text}')

    else:
        responseJSON = response.json()
        print('Results:', responseJSON)
        return responseJSON

def main():
    makeOddsRequest("/americanfootball_ncaaf/odds",
               {'api_key': ODDS_API_KEY, 'regions': REGIONS})
    makeNBARequest()


if __name__ == "__main__":
    main()
