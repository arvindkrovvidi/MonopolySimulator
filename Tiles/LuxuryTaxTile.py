from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile


class LuxuryTaxTile(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

#    TODO: function to be implemented

    def execute(self, player):
        player.bank_transaction(-100)