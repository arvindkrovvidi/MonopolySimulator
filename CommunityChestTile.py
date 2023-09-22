from SpecialTiles import SpecialTiles
from Tile import Tile


class CommunityChestTile(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)