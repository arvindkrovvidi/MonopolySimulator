class Tile:
    def __init__(self, tile_no, name):
        self.tile_no = tile_no
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.tile_no == other.tile_no and self.name == other.name



