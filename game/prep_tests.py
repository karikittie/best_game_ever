import random

from game import Game
from npc import NPC
from player import Player

class test_game(Game):
    def place_ships(self):
        ships = [tuple(['carrier', 5]),
                 tuple(['battleship', 4]),
                 tuple(['submarine', 3]),
                 tuple(['destroyer', 3]),
                 tuple(['patrol', 2])]

        self.players[0].generate_ship_placement(ships)
        self.players[1].generate_ship_placement(ships)

    def start_game(self):
        self.players[0] = NPC()
        self.players[1] = NPC()

        self.place_ships()


        tempPlaya = Player(name="Me")
        tempPlaya.board = self.players[0].board
        tempPlaya.ships = self.players[0].ships
        self.players[0] = tempPlaya

        turn = random.randint(0, 1)

        while True:
            if self.do_turn(self.players[turn], self.players[1-turn]):
                turn = 1 - turn
            else:
                break

        print("{} is the winner!".format(self.players[turn].name))