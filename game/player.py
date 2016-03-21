from board import Board
from ship import Ship


class Player(object):

    def __init__(self, board_size, **kwargs):
        self.board = Board(board_size)
        self.name = 'No Name'
        for key, value in kwargs.items():
            setattr(self, key, value)

    def place_ships(self, size, location, direction, name):



