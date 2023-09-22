from SpecialTiles import SpecialTiles
from Tile import Tile


class ChanceTile(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

    # def execute(self, player):
    #     if self._description == "Advance to Boardwalk":
    #         player.move_to(boardwalk, collect_go_cash_flag=False)
    #     elif self._description == "Advance to Go (Collect $200)":
    #         player.move_to(go)
    #     elif self._description == "Advance to Illinois Avenue. If you pass Go, collect $200":
    #         player.move_to(illinois_avenue)
