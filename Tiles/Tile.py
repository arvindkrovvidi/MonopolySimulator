class Tile:
    def __init__(self, tile_no, name, color_code=''):
        self.tile_no = tile_no
        self.name = name
        self.color_code = color_code

    def __str__(self):
        return f'{self.color_code}{self.name}\033[0m'

    def __eq__(self, other):
        return self.tile_no == other.tile_no and self.name == other.name



