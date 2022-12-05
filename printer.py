class Printer:
    '''Class used to format and print data retrieved from various api's'''

    def formatNBAGames(self, games):
        '''
        format and print a list of nba games

            Parameters:
                games (list): NBA games to print
        '''
        def formatNBAGame(game):
            return f'{game["teams"]["visitors"]["nickname"]} @ {game["teams"]["home"]["nickname"]}'

        gamesList = map(formatNBAGame, games)
        for title in (list(gamesList)):
            print(title)        
