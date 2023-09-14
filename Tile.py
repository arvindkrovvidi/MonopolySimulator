from PropertyIterators import PropertyList


class Tile:
    def __init__(self, tile_no, name):
        self.tile_no = tile_no
        self.name = name


all_properties_list = PropertyList([])


class Property(Tile):

    def __init__(self, tile_no, name, cost, rent):
        Tile.__init__(self, tile_no, name)
        self.cost = cost
        self.rent = rent
        all_properties_list.append(self)

    def __str__(self):
        return self.name


