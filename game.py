from dataclasses import dataclass, InitVar, field
from typing import List
from enum import Enum
from typing import Optional
import io
import chess.pgn

class Result(Enum):
    WIN = 'win'
    TIMEOUT = 'timeout'
    RESIGNED = 'resigned'
    REPETITION = 'repetition'
    CHECKMATED = 'checkmated'
    INSUFFICIENT = 'insufficient'
    AGREED = 'agreed'
    STALEMATE = 'stalemate'
    ABANDONED = 'abandoned'
    TIMEvsINSUFFICIENT = 'timevsinsufficient'
    BUGHOUSE = 'bughousepartnerlose'
    MOVES = '50move'

@dataclass
class PlayerColor:
    rating: int
    username: str
    _result: Result = field(init=False)
    result: InitVar[str]

    def __post_init__(self, result):
        self._result = Result(result)

@dataclass
class Game:
    time_class: str
    white: PlayerColor
    black: PlayerColor
    pgn: InitVar[Optional[str]] = None

    def __post_init__(self, pgn):
        if pgn is not None:
            self.pgn = pgn

    def winning_color(self) -> str:
        if self.white._result == Result.WIN: return 'white'
        elif self.black._result == Result.WIN: return 'black'
        else: return 'draw'

    def user_color(self, username) -> str:
        return 'white' if self.white.username == username else 'black'
    
    def get_pgn(self) -> Optional[chess.pgn.Game]:
        pgnIn = io.StringIO(self.pgn)
        return chess.pgn.read_game(pgnIn)

class UserGame:
    def __init__(self, game, username):
        self.game = game
        self.username = username
        
    def played_as(self) -> str:
        return 'white' if self.game.white.username == self.username else 'black'

    def is_winner(self) -> bool:
        return self.game.user_color(self.username) == self.game.winning_color()

    def result(self) -> str:
        return self.game.white._result if self.game.white.username == self.username else self.game.black._result

    def print_game(self):
        print(self.result() + '\t' + self.played_as() + '\t' + self.game.time_class)

    def opponent_name(self) -> str:
        return self.game.black.username if self.played_as() == 'white' else self.game.white.username
    
    def opponent_rating(self) -> int:
        return self.game.black.rating if self.played_as() == 'white' else self.game.white.rating
    
    def ending_rating(self) -> int:
        return self.game.black.rating if self.played_as() == 'black' else self.game.white.rating


@dataclass
class GameMonth:
    games: List[Game]

    def print_games_for(self, username):
        print()
        for game in self.games:
            userGame = UserGame(game, username)
            userGame.print_game()

@dataclass
class Archive:
    archives: List[str]
