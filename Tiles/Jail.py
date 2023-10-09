from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile
from Tiles_data.special_tiles_data import just_visiting_jail
class Jail(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

    def execute(self, player):
        player.move_to(just_visiting_jail, collect_go_cash_flag=False)
        player.in_jail = False

