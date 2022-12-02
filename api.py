import requests
from dacite import from_dict

from game import *
from user import *

def exists(username) -> bool:
    url = 'https://api.chess.com/pub/player/{}'.format(username)
    response = requests.get(url).json()
    return 'code' not in response.keys()

def get_stats_for(username):
    url = 'https://api.chess.com/pub/player/{}/stats'.format(username)
    statsJson = requests.get(url).json()
    stats = from_dict(UserStats, statsJson)
    stats.print_stats()

def get_games_for(username, month, year):
    url = 'https://api.chess.com/pub/player/{}/games/{}/{}'.format(username, year, month)
    r = requests.get(url)
    gamesJson = r.json()["games"]
    
    for gameJson in gamesJson:
        game = from_dict(Game, gameJson)
        userGame = UserGame(game, 'twopats')
        userGame.print_game()