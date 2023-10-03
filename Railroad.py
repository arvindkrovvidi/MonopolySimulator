from Tile import Tile
class Railroad(Tile):
    def __init__(self, tile_no, name, cost, rent):
        Tile.__init__(self, tile_no, name)
        self.cost = cost
        self._rent = rent
        self._owner = None
        self._colors_owned = 0

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def rent(self):
        return self._rent[self._colors_owned - 1]
