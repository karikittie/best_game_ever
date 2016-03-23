import random

from npc import NPC
from player import Player

class Game:
    def __init__(self, player1=None, player2=None):
        self.players = [player1, player2]

    def is_single_input(self, buffer):
        buf_split = buffer.split()
        return len(buf_split) == 1

    def convert_coordinates_to_indeces(self, coor_str):
        x = int(coor_str[1:]) - 1
        y = ord(coor_str[0].lower())-97
        return tuple([x, y])

    def convert_indeces_to_coordinates(self, coor_tuple):
        return chr(coor_tuple[1]+97) + str(coor_tuple[0]+1)

    def draw_board(self, player, player2=None):
        print("         Yours                     Theirs")
        header = ""
        for idx in range(1, 11):
            header += " {}".format(str(idx))

        cur_row = "  {}    {}".format(header, header)
        print("{}".format(cur_row))

        for idx in range(10):
            cur_row = "{} ".format(chr(idx+65))
            cur_row += player.build_row(True, idx)
            if player2:
                cur_row += "  {} ".format(chr(idx+65))
                cur_row += "{}".format(player2.build_row(False, idx))
            print("{}".format(cur_row))

    def place_ships(self, player):
        ships = [tuple(['carrier', 5]),
                 tuple(['battleship', 4]),
                 tuple(['submarine', 3]),
                 tuple(['destroyer', 3]),
                 tuple(['patrol', 2])]

        if isinstance(player, NPC):
            player.generate_ship_placement(ships)
            return

        for ship in ships:
            self.draw_board(player)
            print("Placing: {}".format(ship[0]))
            print("Size: {}".format(ship[1]))
            while True:

                sbuffer = input("Input starting coordinate (ex: c6): ")
                if not self.is_single_input(sbuffer):
                    print("Input must be a single word")
                    continue

                start_loc = self.convert_coordinates_to_indeces(sbuffer)
                direction = input("Input direction from starting point (N/W/S/E): ")
                if not self.is_single_input(sbuffer):
                    print("Input must be a single word")
                    continue

                if player.place_ship(ship[1], start_loc, direction.lower(), ship[0]):
                    break
                else:
                    print("Invalid placement")

    #TODO: code is repeated, should be refactered
    def do_turn(self, player, other_player):
        if isinstance(player, NPC):
            target = player.fire()
            result = other_player.get_fired_upon(target)
            target = self.convert_indeces_to_coordinates(target)

            # prefix output with player name
            print("{}: ".format(player.name), end='')

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
                if not self.is_single_input(target):
                    print("Error: input must be a single word")
                    continue

                result = other_player.get_fired_upon(self.convert_coordinates_to_indeces(target))

                # prefix output with player name
                print("{}: ".format(player.name), end='')

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
        self.players[0] = Player(name=input('Input your name: '))
        self.players[1] = NPC()

        # place ships for both players
        if input("[p]lace ships or [r]andomize positions?: ").lower() == 'p':
            self.place_ships(self.players[0])
        else:
            temp = NPC()
            self.place_ships(temp)
            self.players[0].board = temp.board
            self.players[0].ships = temp.ships

        # place NPCs ships
        self.place_ships(self.players[1])

        # determine who goes first
        turn = random.randint(0, 1)

        while True:
            if self.do_turn(self.players[turn], self.players[1-turn]):
                turn = 1 - turn
            else:
                break

        print("{} is the winner!".format(self.players[turn].name))
