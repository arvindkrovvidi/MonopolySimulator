from Tiles.Tile import Tile

class Utility(Tile):
    def __init__(self, tile_no, name, cost, rent, color, color_code):
        Tile.__init__(self, tile_no, name, color_code)
        self.cost = cost
        self._rent = rent
        self._owner = None
        self._utilities_owned = 0
        self.color = color

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
        if self not in value.player_portfolio:
            value.player_portfolio.append(self)

    def get_rent(self, throw):
        if self.owner._utilities_owned == 1:
            return 4 * throw
        elif self.owner._utilities_owned == 2:
            return 10 * throw

