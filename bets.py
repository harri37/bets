import os
from requester import Requester
from printer import Printer
from dotenv import load_dotenv
load_dotenv()

ODDS_API_KEY = os.getenv("ODDS_API_KEY")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")

ODDS_URL = "https://api.the-odds-api.com/v4"


NBA_URL = "https://api-nba-v1.p.rapidapi.com"
NBA_HEADERS = {
	"X-RapidAPI-Key": RAPID_API_KEY,
	"X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com"
}

def main():
    nbaRequester = Requester(NBA_URL)
    oddsRequester = Requester(ODDS_URL)
    nbaPrinter = Printer()
    nbaResponse = nbaRequester.makeRequest("/games", NBA_HEADERS, {"date": "2022-12-06"})
    nbaPrinter.formatNBAGames(nbaResponse["response"])
    #oddsRequester.makeRequest("/sports", params={"api_key": ODDS_API_KEY})

if __name__ == "__main__":
    main()
