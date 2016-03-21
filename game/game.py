from player import Player
from npc import NPC

class Game:
    def __init__(self, player1=Player(), player2=NPC()):
        self.player1 = player1
        self.player2 = player2

    def convert_coordinates(self, buffer):
        return tuple([buffer[1], ord(buffer[0])-97])

    #def draw_board(self):

    def set_ships(self, player):
        ships = [tuple(['carrier', 5]),
                 tuple(['battleship', 4]),
                 tuple(['submarine', 3]),
                 tuple(['destroyer', 3]),
                 tuple(['patrol', 2])]

        for ship in ships:
            while True:
                draw_own_board()
                sbuffer = input("Input starting coordinate (ex: c6): ")
                start_loc = self.convert_coordinates(sbuffer)
                direction = input("Input direction from starting point (N/W/S/E): ")
                if player.place_ship(ship[1], start_loc, direction, ship[0]):
                    break
                else:
                    print("Invalid placement")

    #def do_turn(self):

    #def start_game(self):