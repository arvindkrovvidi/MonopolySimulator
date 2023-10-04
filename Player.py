import random

from Board import max_tile_no, go_cash
from TileIterators import TileList
from utils import check_player_has_color_set


class Player:
    def __init__(self, name, cash=200, tile_no=0, networth=0):
        self._player_portfolio = TileList([])
        self.tile_no = tile_no
        self.name = name
        self.cash = cash
        self.networth = networth

    # @property
    # def tile_no(self):
    #     return self._tile_no

    @property
    def player_portfolio(self):
        return self._player_portfolio

    @player_portfolio.setter
    def player_portfolio(self, value):
        self._player_portfolio.append(value)

    def __str__(self):
        return self.name

    def buy_property(self, asset) -> None:
        """
        Buy property that the player lands on.
        :param asset: Property
        """
        if asset.cost <= self.cash:
            self.cash -= asset.cost
            self.player_portfolio.append(asset)
            asset.owner = self
            if check_player_has_color_set(self, asset.color):
                asset._color_set = True


    def throw_dice(self) -> int:
        """
        Simulates a two dice throw by generating a random number between 2 and 12.
        :return: Random integer between 2 and 12
        """
        return random.randint(2, 12)

    def move(self, throw: int) -> None:
        """
        Move the player to a tile based on the dice throw
        :param throw: The dice throw
        """
        self.tile_no += throw
        if self.tile_no  > max_tile_no:
            self.tile_no -= (max_tile_no + 1)
            if self.tile_no == 0:
                pass
            else:
                self.cash += go_cash
    def move_to(self, tile, collect_go_cash_flag: bool=True) -> None:
        """
        Move to a specific Tile with or without collecting salary. This occurs through Chance, Community chest cards and Jail tiles.
        :param tile: The tile to move to
        :param collect_go_cash_flag: True if salary is to be collected. Else False.
        """
        self.tile_no = tile.tile_no
        if collect_go_cash_flag:
            self.cash += 200

    def pay_rent(self, player, rent: int) -> None:
        """
        Pay rent to the specified player
        :param player: The player to whom the rent has to be paid
        :param rent: The rent to be paid to the player
        """
        self.cash -= rent
        player.cash += rent

    def player_transaction(self, player, amount: int) -> None:
        """
        Collect or pay a player a specified amount. Positive means collect from player. Negative means pay player.
        :param player: The player paying
        :param amount: The amount being paid
        """
        self.cash += amount
        player.cash -= amount

    def bank_transaction(self, amount: int) -> None:
        """
        Collect or pay the bank a certain amount
        :param amount: The amount being paid or collected
        """
        self.cash += amount


    def build_house(self, asset):
        """
        Build a house in a property
        :param asset: A property where house is being built
        """
        if asset.building_cost <= self.cash:
            asset._houses += 1
            self.cash -= asset.building_cost
