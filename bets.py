import os
from datetime import datetime
import numpy as np
import pandas as pd
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

def calculateRankings(games, teams):
    
    def getWinnerAndLoser(game):
        winners = ("home" 
        if game["scores"]["home"]["points"] > game["scores"]["visitors"]["points"] 
        else "visitors")
        losers = "visitors" if winners == "home" else "home"
        winersIndex = list(filter(lambda team: team["name"] == 
        game["teams"][winners]["name"], teams))[0]["id"] 
        losersIndex = list(filter(lambda team: team["name"] == 
        game["teams"][losers]["name"], teams))[0]["id"]
        return winersIndex, losersIndex 

    def getRecencyBiases():
        currentDate = datetime.now()
        gameDates = list()
        for game in games:
            gameDates.append(datetime.strptime(game["date"]["end"], "%Y-%m-%dT%H:%M:%S.000Z"))
        print(gameDates)

    recencyBiases = getRecencyBiases()
    domMat = np.zeros([len(teams), len(teams)])

    for game in games:

        winner, loser = getWinnerAndLoser(game)
        domMat[winner][loser] += 1
        if game["teams"]["visitors"]["name"] == teams[winner]["name"]:
            domMat[winner][loser]  += 0.5

    domMat2 = np.matmul(domMat, domMat)
    domMat3 = np.matmul(domMat2, domMat)

    domSum = domMat + 0.5 * domMat2 + 0.3 * domMat3
    domRowSum = np.sum(domSum, axis=1)
    dtype = [('teamName', 'S25'), ('score', float)]
    teamValues = [(teams[index]["name"], value) for index, value in enumerate(domRowSum)]
    teamValuesArray = np.array(teamValues, dtype=dtype)
    sortedScores = np.flip(np.sort(teamValuesArray, order='score'))
    return sortedScores




def filterGames(games, teams):
    validTeamNames = list(map(lambda team: team["name"], teams))
    return list(filter(lambda game: game["status"]["long"] == "Finished" 
    and game["teams"]["home"]["name"] in validTeamNames 
    and game["teams"]["visitors"]["name"] in validTeamNames, games))

def filterTeams(teams):
    nbaTeams = list(filter(lambda team: team["nbaFranchise"] == True 
    and team["name"] != "Home Team Stephen A", teams))

    for index, team in enumerate(nbaTeams):
        team["id"] = index
    return nbaTeams 

def main():
    nbaRequester = Requester(NBA_URL)
    #oddsRequester = Requester(ODDS_URL)
    nbaPrinter = Printer()
    nbaGames = nbaRequester.makeRequest("/games", NBA_HEADERS, {"season": 2022})
    nbaTeams = filterTeams(nbaRequester.makeRequest("/teams", NBA_HEADERS)["response"])
    finishedGames = filterGames(nbaGames["response"], nbaTeams)
    rankings = calculateRankings(finishedGames, nbaTeams)
    nbaPrinter.formatRankings(rankings)

    #oddsRequester.makeRequest("/sports", params={"api_key": ODDS_API_KEY})

if __name__ == "__main__":
    main()
