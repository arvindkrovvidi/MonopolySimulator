import random

from Board import max_tile_no, go_cash
from TileIterators import TileList
from Tiles.Utility import Utility
from errors import PlayerBrokeError, PropertyNotFreeError
from utils import check_player_has_color_set, check_property_can_be_developed, check_can_build_hotel, \
    set_color_set_value


class Player:
    def __init__(self, name, cash=200, tile_no=0, networth=0):
        self._player_portfolio = TileList([])
        self.tile_no = tile_no
        self.name = name
        self.cash = cash
        self.networth = networth
        self._railroads_owned = 0
        self._utilities_owned = 0
        self.double_counter = 0
        self.get_out_of_jail_free_card = 0
        self.in_jail = False
        self.jail_throw_counter = 0


    @property
    def player_portfolio(self):
        return self._player_portfolio

    @player_portfolio.setter
    def player_portfolio(self, value):
        self._player_portfolio.append(value)

    @property
    def railroads_owned(self):
        return self._railroads_owned

    @railroads_owned.setter
    def railroads_owned(self, value):
        self._railroads_owned = value

    @property
    def utilities_owned(self):
        return self._utilities_owned

    @utilities_owned.setter
    def utilities_owned(self, value):
        self._utilities_owned = value

    def __str__(self):
        return self.name

    def buy_property(self, asset) -> None:
        """
        Buy property that the player lands on (excluding railroads and utilities).
        :param asset: Property
        """
        if asset.owner is not None:
            raise PropertyNotFreeError(asset)
        if asset.cost <= self.cash:
            self.cash -= asset.cost
            self.player_portfolio.append(asset)
            asset.owner = self
            if check_player_has_color_set(self, asset.color):
                set_color_set_value(self, asset)


    def buy_railroad(self, asset):
        """
        Buy railroad that the player lands on
        :param asset: Railroad
        """
        if asset.cost <= self.cash:
            self.cash -= asset.cost
            self.player_portfolio.append(asset)
            asset.owner = self
            if self.railroads_owned < 4:
                self.railroads_owned += 1
            if check_player_has_color_set(self, asset.color):
                asset._color_set = True

    def buy_utility(self, asset):
        """
        Buy the utility that the player lands on
        :param asset: Utility
        """
        if asset.cost <= self.cash:
            self.cash -= asset.cost
            self.player_portfolio.append(asset)
            asset.owner = self
            if type(asset) == Utility and self.utilities_owned < 2:
                self.utilities_owned += 1
            if check_player_has_color_set(self, asset.color):
                asset._color_set = True

    def throw_one_dice(self):
        return random.randint(1, 6)

    def throw_dice(self) -> int:
        """
        Simulates a two dice throw by generating a random number between 2 and 12.
        :return: Random integer between 2 and 12
        """
        dice1 = self.throw_one_dice()
        dice2 = self.throw_one_dice()
        if dice1 == dice2:
            self.double_counter += 1
        else:
            self.double_counter = 0
        return dice1 + dice2

    def move(self, throw: int) -> None:
        """
        Move the player to a tile based on the dice throw. Positive throw means move forward. Negative throw means move backward.
        :param throw: The dice throw
        """
        if not self.in_jail:
            self.tile_no += throw
            if self.tile_no == 30:
                self.in_jail = True
            if self.tile_no < 0:
                self.tile_no = 40 + throw
            if self.tile_no  > max_tile_no:
                self.tile_no -= (max_tile_no + 1)
                if self.tile_no == 0:
                    pass
                else:
                    self.cash += go_cash

    def move_to(self, tile_no, collect_go_cash_flag: bool=True) -> None:
        """
        Move to a specific Tile with or without collecting salary. This occurs through Chance, Community chest cards and Jail tiles.
        :param tile_no: The tile number to move to
        :param collect_go_cash_flag: True if salary is to be collected. Else False.
        """
        self.tile_no = tile_no
        if collect_go_cash_flag:
            self.cash += 200
        if tile_no == 10:
            self.in_jail = True

    def pay_rent(self, player, rent: int) -> None:
        """
        Pay rent to the specified player
        :param player: The player to whom the rent has to be paid
        :param rent: The rent to be paid to the player
        """
        if self.cash - rent < 0:
            print(f'{self} cannot pay {player} rent of {rent}')
            raise PlayerBrokeError(player)
        self.cash -= rent
        player.cash += rent

    def player_transaction(self, player, amount: int) -> None:
        """
        Collect or pay a player a specified amount
        :param player: The player paying
        :param amount: The amount being paid. Positive means collect from player. Negative means pay player.
        """
        if self.cash + amount < 0:
            print(f'{self} cannot pay {player} amount of {-amount}')
            raise PlayerBrokeError
        self.cash += amount
        player.cash -= amount

    def bank_transaction(self, amount: int) -> None:
        """
        Collect or pay the bank a certain amount
        :param amount: The amount being paid or collected
        """
        if self.cash + amount < 0:
            print(f'{self} cannot pay the bank amount of {-amount}')
            raise PlayerBrokeError(self)
        self.cash += amount


    def build_house(self, asset):
        """
        Build a house in a property if player has the color set and the property can be developed.
        :param asset: A property where house is being built
        """
        if asset.building_cost <= self.cash and check_player_has_color_set(self, asset.color) and check_property_can_be_developed(asset):
            asset._houses += 1
            self.cash -= asset.building_cost

    def build_hotel(self, asset):
        """
        Build hotel in property
        :param asset: The tile where the hotel is being built
        """
        if check_can_build_hotel(asset) and self.cash > asset.building_cost:
            asset._hotel = True
            self.cash -= asset.building_cost

    def pay_jail_fine(self):
        """
        Pay fine to get out of jail
        """
        if self.cash > 50:
            self.bank_transaction(-50)
            self.in_jail = False

    def try_jail_double_throw(self):
        """
        Try to throw a double to get out of jail. You get three turns to throw a double. After three turns, you pay the fine.
        """
        dice1 = self.throw_one_dice()
        dice2 = self.throw_one_dice()
        if dice1 == dice2:
            self.in_jail = False
        self.jail_throw_counter += 1
        if self.jail_throw_counter == 3:
            self.pay_jail_fine()
            self.in_jail = False
            self.jail_throw_counter = 0

    def get_out_of_jail_free(self):
        """
        Use get out of jail free card.
        """
        self.get_out_of_jail_free_card -= 1
        self.in_jail = False