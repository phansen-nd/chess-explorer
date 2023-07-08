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
    gamesJson = requests.get(url).json()
    games = from_dict(GameMonth, gamesJson)
    games.print_games_for(username)

def get_game_archive(username) -> Archive:
    url = 'https://api.chess.com/pub/player/{}/games/archives'.format(username)
    archivesJson = requests.get(url).json()
    return from_dict(Archive, archivesJson)

def get_all_games(username) -> List[UserGame]:
    archive = get_game_archive(username)
    games = []
    totalCount = len(archive.archives)
    completedCount = 0
    print("Getting {} months of games".format(totalCount))
    for url in archive.archives:
        gamesJson = requests.get(url).json()
        games += from_dict(GameMonth, gamesJson).games
        completedCount += 1
        print("Completed {}/{}".format(completedCount, totalCount))
        
    return list(map(lambda game: UserGame(game, username), games))
