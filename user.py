from dataclasses import dataclass

@dataclass
class LastStats: 
    rating: int
    date: int # seconds since epoch

@dataclass
class BestStats:
    rating: int
    date: int

@dataclass
class Record:
    win: int
    loss: int
    draw: int

@dataclass
class TypeStats:
    last: LastStats
    best: BestStats
    record: Record

    def to_str(self) -> str:
        return str(self.last.rating) + '\t' + \
                str(self.best.rating) + '\t' + \
                str(self.record.win) + ' / ' + str(self.record.loss) + \
                ' (' + str(self.record.draw) + ')'

@dataclass
class UserStats:
    chess_rapid: TypeStats
    chess_bullet: TypeStats
    chess_blitz: TypeStats

    def print_stats(self):
        print('type\tcurrent\tbest\trecord (w/l(d))')
        print('rapid\t' + self.chess_rapid.to_str())
        print('blitz\t' + self.chess_blitz.to_str())
        print('bullet\t' + self.chess_bullet.to_str())