import random

from npc import NPC
from player import Player

class Game:
    def __init__(self, player1=None, player2=None):
        self.players = [player1,player2]

    def convert_coordinates(self, buffer):
        x = int(buffer[1:]) - 1
        y = ord(buffer[0])-97
        return tuple([x, y])

    #TODO: draw column/row headers
    def draw_board(self, player, player2=None):
        for idx in range(10):
            cur_row = player.build_row(True, idx)
            if player2:
                cur_row += "  {}".format(player2.build_row(False, idx))
            print("{}".format(cur_row))

    def place_ships(self, player):
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

    #TODO: code is repeated, should be refactered
    def do_turn(self, player, other_player):
        if isinstance(player, NPC):
            target = player.fire()
            result = other_player.get_fired_upon(target)
            if result == 0:
                print("{} missed!".format(target))
            else:
                print("{} hit!".format(target), end='')
                sunk_ship = other_player.update_ships_status()
                if sunk_ship:
                    print(" {} was sunk!".format(sunk_ship))
                else:
                    print(" {} took damage!".format(result.name))
                if other_player.is_game_over():
                    return False
        else:
            self.draw_board(player, other_player)
            while True:
                target = input("Input target coordinates (ex: h5): ")
                result = other_player.get_fired_upon(self.convert_coordinates(target))
                if result == 0:
                    print("{} missed!".format(target))
                    break
                elif result == 2:
                    print("{} is not a valid target coordinate.".format(target))
                else:
                    print("{} hit!".format(target), end='')
                    sunk_ship = other_player.update_ships_status()
                    if sunk_ship:
                        print(" {} was sunk!".format(sunk_ship))
                    else:
                        print(" {} took damage!".format(result.name))
                    if other_player.is_game_over():
                        return False
                    break
        return True

    def start_game(self):
        # Create players
        self.players[0] = Player(name='player1')
        self.players[1] = NPC()

        # setup AI
        self.players[1]

        # place ships for both players
        self.place_ships(self.players[0])
        self.place_ships(self.players[1])

        # determine who goes first
        turn = random.randint(0, 1)

        while True:
            if self.do_turn(self.players[turn], self.players[1-turn]):
                turn = 1 - turn
            else:
                break

        print("{} is the winner!".format(self.players[turn].name))
