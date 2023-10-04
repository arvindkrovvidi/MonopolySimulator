from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile


class IncomeTaxTile(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)
#    TODO: function to be implemented
    @staticmethod
    def execute(player, card_no):
        pass
