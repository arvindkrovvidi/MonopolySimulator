from Tile import Tile


class Property(Tile):

    def __init__(self, tile_no, name, cost, rent):
        Tile.__init__(self, tile_no, name)
        self.cost = cost
        self._rent = rent
        self._owner = None
        self._color_set = True
        self._houses = 0
        self._hotel = False

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        self._owner = value

    @property
    def rent(self):
        if not self._color_set:
            return self._rent["Site"]
        if self._houses != 0:
            if self._hotel:
                return self._rent["Hotel"]
            else:
                return self._rent["House"][self._houses - 1]
        return self._rent["Color Set"]



