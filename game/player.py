from board import Board
from ship import Ship


class Player(object):

    def __init__(self, board_size=(10,10), **kwargs):
        self.ships = []
        self.board = Board(board_size)
        self.name = 'No Name'
        for key, value in kwargs.items():
            setattr(self, key, value)

    def place_ship(self, size, location, direction, name):
        if direction == 's':
            locations = [(location[0], y) for y in range(location[1], location[1]+size)]
        elif direction == 'n':
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

    def get_fired_upon(self, location):

        success = self.board.fire(location)
        if success == 1:
            return next(ship for ship in self.ships if list(filter(lambda x: x == location, ship.location)))
            # for ship in self.ships:
            #    if next((loc for loc in ship.location if loc == location)):
            #        return ship.name
        else:
            return success

    def update_ships_status(self):
        for ship in self.ships:
            if ship.sunk_state:
                continue
            sunk = True
            for location in ship.location:
                if not self.board.get_index(location).is_hit:
                    sunk = False
            if sunk:
                ship.sunk_state = True
                return ship.name
        return None

    def is_game_over(self):
        for ship in self.ships:
            if not ship.sunk_state:
                return False
        return True

    def build_row(self, is_me, row):
        return self.board.build_row(is_me, row)
