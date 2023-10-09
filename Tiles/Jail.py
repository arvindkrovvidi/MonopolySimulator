from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile
class Jail(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

    def execute(self, player):
        player.move_to(10, collect_go_cash_flag=False)
        player.in_jail = False

