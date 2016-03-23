import random


from board import Board
from player import Player


class NPC(Player):
    def __init__(self, size=(10,10)):
        self.ships = []
        self.board = Board(size)
        self.name = 'Artificial Stupidity'
        self.spot_list = [(x,y) for x in range(size[0]) for y in range(size[1])]
        self.x_max = size[0]
        self.y_max = size[1]

    def generate_ship_placement(self, ships_list):
        for ship in ships_list:
            while True:
                if self.place_ship(ship[1],
                                  (random.randint(0, self.x_max),random.randint(0, self.y_max)),
                                  random.choice('nsew'),
                                  ship[0]):
                    break

    def fire(self):
        return self.spot_list.pop(random.randint(0, len(self.spot_list)-1))
