from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile
from utils import randomly_play_jail_turn
class Jail(SpecialTiles):
    def __init__(self, tile_no, name, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

    def execute(self, player):
        randomly_play_jail_turn(player)