from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile


class IncomeTaxTile(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

    def execute(self, player):
        player.bank_transaction(-200)
