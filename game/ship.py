
class Ship:
    sunk_state = False

    def __init__(self, name="unnamed ship", location=list()):
        self.name = name
        self.location = location

    def __str__(self):
        print("Ship name: {}".format(self.name))

    def get_location(self):
        return self.location