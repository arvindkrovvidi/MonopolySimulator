from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile


class FreeParkingTile(SpecialTiles):
    def __init__(self, tile_no, name, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

    def execute(self, player):
        pass