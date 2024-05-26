from Tiles.Tile import Tile

class Utility(Tile):
    def __init__(self, tile_no, name, cost, rent, color, color_code):
        Tile.__init__(self, tile_no, name, color_code)
        self.cost = cost
        self._rent = rent
        self._owner = None
        self.color = color
        self.mortgaged = False
        self.mortgage_value = self.cost / 2
        self.unmortgage_cost = round((self.cost / 2) * 1.1, 1)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value
        if value is not None:
            if self not in value.player_portfolio:
                value.player_portfolio.append(self)

    def get_rent(self, throw):
        if self.mortgaged:
            return 0
        utilities_owned = len([asset for asset in self.owner.player_portfolio if type(asset) is Utility])
        if utilities_owned == 1:
            return 4 * throw
        elif utilities_owned == 2:
            return 10 * throw

