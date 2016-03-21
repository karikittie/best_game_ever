from board import Board
from ship import Ship


class Player(object):
    ships = []

    def __init__(self, board_size, **kwargs):
        self.board = Board(board_size)
        self.name = 'No Name'
        for key, value in kwargs.items():
            setattr(self, key, value)

    def place_ships(self, size, location, direction, name):
        if direction == 'n':
            locations = [(location[0], y) for y in range(location[1], location[1]+size)]
        elif direction == 's':
            locations = [(location[0], location[1]-y) for y in range(size)]
        elif direction == 'e':
            locations = [(x, location[1]) for x in range(location[0], location[0]+size)]
        elif direction == 'w':
            locations = [(location[0]-x, location[1]) for x in range(size)]
        if self.board.place_ship(locations):
            self.ships.append(Ship(name, locations))
            return True
        else:
            return False