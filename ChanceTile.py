from Tile import Tile
class ChanceTile(Tile):
    def __init__(self, description, name, tile_no):
        self._description = description
        Tile.__init__(self, tile_no, name)

    # def execute(self, player):
    #     if self._description == "Advance to Boardwalk":
# test commit

