from dataclasses import dataclass

@dataclass
class PlayerColor:
    rating: int
    result: str
    username: str

@dataclass
class Game:
    time_class: str
    white: PlayerColor
    black: PlayerColor

    def winning_color(self) -> str:
        if self.white.result == 'win': return 'white'
        elif self.black.result == 'win': return 'black'
        else: return 'draw'

    def user_color(self, username) -> str:
        return 'white' if self.white.username == username else 'black'    

class UserGame:
    def __init__(self, game, username):
        self.game = game
        self.username = username
        
    def played_as(self) -> str:
        return 'white' if self.game.white.username == self.username else 'black'

    def is_winner(self) -> bool:
        return self.game.user_color(self.username) == self.game.winning_color()

    def result(self) -> str:
        if self.game.winning_color() == 'draw': return '-'
        return 'w' if self.is_winner() else 'l'

    def print_game(self):
        print(self.result() + '\t' + self.played_as() + '\t' + self.game.time_class)
