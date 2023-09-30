import random

from Board import max_tile_no, go_cash
from Property_data import property_tracker
from TileIterators import TileList


class Player:
    def __init__(self, name, cash=200, tile_no=0, networth=0):
        self._player_portfolio = TileList([])
        self.tile_no = tile_no
        self.name = name
        self.cash = cash
        self.networth = networth

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
            property_tracker.update_dict({asset: self})

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
        self.tile_no = tile.tile_no
        if collect_go_cash_flag:
            self.cash += 200

    def pay_rent(self, player, rent: int) -> None:
        self.cash -= rent
        player.cash += rent

    def pay_player(self, player, amount):
        """
        Pay a player a specified amount
        :param player: The player paying
        :param amount: The amount being paid
        """
        self.cash -= amount
        player.cash += amount

