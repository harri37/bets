class Printer:
    '''Class used to format and print data retrieved from various api's'''

    def formatNBAGames(self, games):
        '''
        format and print a list of nba games

            Parameters:
                games (list): NBA games to print
        '''
        def formatNBAGame(game):
            return f'{game["teams"]["visitors"]["nickname"]} - {game["scores"]["visitors"]["points"]} @ {game["teams"]["home"]["nickname"]} - {game["scores"]["home"]["points"]}'

        gamesList = map(formatNBAGame, games)
        for title in (list(gamesList)):
            print(title)        

    def formatNbaTeams(self, teams):

        print(f'{len(teams)} teams')

        for team in (teams):
            print(f'{team["name"]} id: {team["id"]}')

    def formatRankings(self, rankings):
        for index, rank in enumerate(rankings):
            print(f'{index + 1}: {rank[0].decode()} {rank[1]}pts')