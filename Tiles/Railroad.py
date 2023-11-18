from Tiles.Tile import Tile
class Railroad(Tile):
    def __init__(self, tile_no, name, cost, rent, color, color_code):
        Tile.__init__(self, tile_no, name, color_code)
        self.cost = cost
        self._rent = rent
        self._owner = None
        self.color = color
        self.mortgaged = False

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
        if value is not None:
            if self not in value.player_portfolio:
                value.player_portfolio.append(self)

    @property
    def rent(self):
        if self.mortgaged:
            return 0
        railroads_owned = len([asset for asset in self.owner.player_portfolio if type(asset) is Railroad])
        return self._rent[railroads_owned - 1]
