from Tiles.Tile import Tile
from config import printing_and_logging


class Property(Tile):

    def __init__(self, tile_no, name, cost, rent, color, building_cost, color_code):
        super().__init__(tile_no, name, color_code)
        self.cost = cost
        self.color = color
        self._rent = rent
        self._owner = None
        self._color_set = False
        self._houses = 0
        self._hotel = False
        self._building_cost = building_cost
        self.mortgaged = False

    def __eq__(self, other):
        if self.name == other.name and self.tile_no == other.tile_no and self.cost == other.cost and self.color == other.color:
            return True

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
        if self.mortgaged:
            return 0
        if not self._color_set:
            return self._rent["Site"]
        if self._houses != 0:
            if self._hotel:
                return self._rent["Hotel"]
            else:
                return self._rent["House"][self._houses - 1]
        return self._rent["Color Set"]


    @property
    def building_cost(self):
        return self._building_cost

    @building_cost.setter
    def building_cost(self):
        if 1 <= self.tile_no <= 9:
            self._building_cost = 50
        elif 11 <= self.tile_no <= 19:
            self._building_cost = 100
        elif 21 <= self.tile_no <= 29:
            self._building_cost = 150
        elif 31<= self.tile_no <= 39:
            self._building_cost = 200