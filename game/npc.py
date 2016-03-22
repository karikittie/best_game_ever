import random


from board import Board
from player import Player


class NPC(Player):
    def __init__(self, size=(10,10)):
        self.board = Board(size)
        self.name = 'computer player'

    def place_ships(self, ships_list):
