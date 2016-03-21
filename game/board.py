class Tile(object):
    def __init__(self, occupied=False):
        self.is_occupied = occupied
        self.is_hit = False

    def show_other(self):
        logo = 'O'
        if self.is_hit and self.is_occupied:
            logo = '&'
        elif self.is_hit:
            logo = 'X'
        print("|{}|".format(logo))

    def show_me(self):
        logo = 'O'
        if self.is_hit and self.is_occupied:
            logo = '&'
        elif self.is_hit and not self.is_occupied:
            logo = '*'
        elif self.is_occupied:
            logo = 'X'
        print("|{}|".format(logo))


class Board(object):
    def __init__(self, board_size=(10,10)):
        self.x_max = board_size[0]
        self.y_max = board_size[1]
        self.board = [[(x, y), Tile()] for x in range(board_size[0]) for y in range(board_size[1])]

    def place_ship(self, locations):
        for location in locations:
            if location[0] >= self.x_max or location[1] >= self.y_max:
                return None
            index = location[1] * self.x_max + location[0]
            if self.board[index][1].is_occupied:
                return None
        tile_list = []
        for tile in locations:
            index = tile[1] * self.x_max + tile[0]
            self.board[index][1].is_occupied = True
            tile_list.append(index)
        return tile_list

    def fire(self, location):
        if location[0] >= self.x_max:
            return 2
        elif location[1] >= self.y_max:
            return 2
        index = location[1] * self.x_max + location[0]
        board_tile = self.board[index][1]
        if board_tile.is_occupied and not board_tile.is_hit:
            board_tile.is_hit = True
            return 1
        elif board_tile.is_hit:
            return 2
        else:
            board_tile.is_hit = True
            return 0

    def get_index(self, index):
        return self.board[index][1]