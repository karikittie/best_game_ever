from board import Tile

class Ship:
    sunk_state = False

    def __init__(self, name="unnamed ship", location=list()):
        self.name = name
        self.location = location

    def __str__(self):
        print("Ship name: {}".format(self.name))

    def isSunk(self):
        hp = len(location)
        for tile in location:
            if tile.hit_state:
                hp -= 1
        if hp == 0:
            return True
        return False