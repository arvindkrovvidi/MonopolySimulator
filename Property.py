from Tile import Tile


class Property(Tile):

    def __init__(self, tile_no, name, cost, rent):
        Tile.__init__(self, tile_no, name)
        self.cost = cost
        self.rent = rent

    def __str__(self):
        return self.name
