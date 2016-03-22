import random

from npc import NPC
from player import Player

class Game:
    def __init__(self, player1=None, player2=None):
        self.players = [player1,player2]

    def convert_coordinates(self, buffer):
        return tuple([buffer[1], ord(buffer[0])-97])

    #TODO: draw column/row headers
    def draw_board(self, player, player2=None):
        for idx in range(10):
            player.build_row(idx)
            if player2:
                player2.build_row(idx)

    def set_ships(self, player):
        ships = [tuple(['carrier', 5]),
                 tuple(['battleship', 4]),
                 tuple(['submarine', 3]),
                 tuple(['destroyer', 3]),
                 tuple(['patrol', 2])]

        if isinstance(player,NPC):
            player.generate_ship_placement(ships)
            return

        for ship in ships:
            while True:
                self.draw_board(player)
                sbuffer = input("Input starting coordinate (ex: c6): ")
                start_loc = self.convert_coordinates(sbuffer)
                direction = input("Input direction from starting point (N/W/S/E): ")
                if player.place_ship(ship[1], start_loc, direction.lower(), ship[0]):
                    break
                else:
                    print("Invalid placement")

    def do_turn(self, player, other_player):
        if isinstance(player,NPC):
            other_player.get_fired_upon(player.fire())
        else:
            while True:
                target = input("Input target coordinates (ex: h5): ")
                result = player.get_fired_upon(self.convert_coordinates(target))
                if result == 0:
                    print("{} missed!".format(target))
                    break
                elif result == 1:
                    print("{} hit!".format(target), end='')
                    sunk_ship = other_player.update_ships_status()
                    if sunk_ship:
                        print(" {} was sunk!".format(sunk_ship))
                    else:
                        print("")
                    if other_player.is_game_over():
                        return False
                else:
                    print("{} is not a valid target coordinate.".format(target))
            return True

    def start_game(self):
        #Create players
        self.players[0] = Player('name'='player1')
        self.player[1] = NPC()

        #setup AI
        self.players[1]

        #place ships for both players
        self.set_ships(self.players[0])
        self.set_ships(self.player[1])

        #determine who goes first
        turn = random.randInt(0,1)

        while True:
            if self.do_turn(self.players[turn],self.players[1-turn]):
                turn = 1 - turn
            else:
                break

        print("{} is the winner!".format(self.players[turn].name))