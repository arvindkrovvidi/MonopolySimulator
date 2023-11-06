from Tiles.Tile import Tile
class Railroad(Tile):
    def __init__(self, tile_no, name, cost, rent, color, color_code):
        Tile.__init__(self, tile_no, name, color_code)
        self.cost = cost
        self._rent = rent
        self._owner = None
        self.color = color

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
        if self not in value.player_portfolio:
            value.player_portfolio.append(self)

    @property
    def rent(self):
        return self._rent[self.owner._railroads_owned - 1]
