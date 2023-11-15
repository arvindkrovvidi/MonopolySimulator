import random

from Board import max_tile_no, go_cash
from TileIterators import TileList
from Tiles.Property import Property
from Tiles.Railroad import Railroad
from Tiles.Utility import Utility
from Tiles_data.all_tiles_data import all_tiles_list
from config import logger, printing_and_logging
from errors import PlayerBrokeError, CannotBuildHouseError, \
    CannotBuildHotelError, CannotSellHouseError, InvalidPropertyTypeError, CannotSellHotelError
from utils import check_player_has_color_set, check_can_build_hotel, \
    set_color_set_value, check_can_sell_house, check_can_sell_hotel, check_can_buy_asset, check_can_build_house, \
    UnownedPropertyError, PropertyNotFreeError


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
        self._current_tile = all_tiles_list[self.tile_no]

    @property
    def current_tile(self):
        return self._current_tile

    @current_tile.setter
    def current_tile(self, tile):
        self._current_tile = tile

    @property
    def player_portfolio(self):
        return self._player_portfolio


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

    def buy_asset(self, asset) -> None:
        """
        Buy asset that the player lands on.
        :param asset: Property, Railroad or Utility.
        """
        if check_can_buy_asset(self, asset):
            self.bank_transaction(-asset.cost)
            self.player_portfolio.append(asset)
            asset.owner = self
        if type(asset) is Property:
            if check_player_has_color_set(self, asset.color):
                set_color_set_value(self, asset)
        elif type(asset) is Railroad:
            if self.railroads_owned < 4:
                self.railroads_owned += 1
            if check_player_has_color_set(self, asset.color):
                asset._color_set = True
        elif type(asset) is Utility:
            if self.utilities_owned < 2:
                self.utilities_owned += 1
            if check_player_has_color_set(self, asset.color):
                asset._color_set = True
        printing_and_logging(f'{self} bought {asset}.')


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
            printing_and_logging(f'{self} threw a double: {dice1} and {dice2}. Total: {dice1 + dice2}')
        else:
            self.double_counter = 0
            printing_and_logging(f'{self} threw a {dice1 + dice2}')
        if self.double_counter == 3:
            self.in_jail = True
            printing_and_logging(f'{self} threw three doubles in a row.')
        return dice1 + dice2

    def move(self, throw: int) -> None:
        """
        Move the player to a tile based on the dice throw. Positive throw means move forward. Negative throw means move backward.
        :param throw: The dice throw
        """
        if not self.in_jail:
            self.tile_no += throw
            if self.tile_no < 0:
                self.tile_no = 40 + throw
            if self.tile_no  > max_tile_no:
                self.tile_no -= (max_tile_no + 1)
                if self.tile_no == 0:
                    pass
                else:
                    self.bank_transaction(go_cash)
                    printing_and_logging(f'{self} collected {go_cash} for passing Go')

    def move_to(self, tile_no, collect_go_cash_flag: bool=True) -> None:
        """
        Move to a specific Tile with or without collecting salary. This occurs through Chance, Community chest cards and GoToJail tiles.
        :param tile_no: The tile number to move to
        :param collect_go_cash_flag: True if salary is to be collected. Else False.
        """
        self.tile_no = tile_no
        if collect_go_cash_flag:
            self.bank_transaction(go_cash)
            printing_and_logging(f'{self} collected {go_cash} for passing Go')
        if tile_no == 10:
            self.in_jail = True
        printing_and_logging(f'{self} moved to {all_tiles_list[tile_no]}')

#TODO: Change function such that it takes property as input instead of rent amount
    def pay_rent(self, player, rent: int) -> None:
        """
        Pay rent to the specified player
        :param player: The player to whom the rent has to be paid
        :param rent: The rent to be paid to the player
        """
        if player == self:
            return
        if self.cash - rent < 0:
            raise PlayerBrokeError(player)
        self.player_transaction(player, -rent)
        printing_and_logging(f'{self} paid {player} rent of amount {rent}')

    def player_transaction(self, player, amount: int) -> None:
        """
        Collect or pay a player a specified amount
        :param player: The player paying
        :param amount: The amount being paid. Positive means collect from player. Negative means pay player.
        """
        if self.cash + amount < 0:
            printing_and_logging(f'{self} cannot pay {player} amount of {-amount}')
            raise PlayerBrokeError(self)
        self.cash += amount
        player.cash -= amount
        if amount > 0:
            printing_and_logging(f'{self} collected {amount} from {player}')
        else:
            printing_and_logging(f'{self} paid {player} an amount of {-amount}')

    def bank_transaction(self, amount: float) -> None:
        """
        Collect or pay the bank a certain amount.
        :param amount: The amount being paid or collected. Amount is positive for collection. Negative for payment.
        """
        if self.cash + amount < 0:
            printing_and_logging(f'{self} cannot pay the bank an amount of {-amount}')
            raise PlayerBrokeError(self)
        self.cash += amount
        if amount > 0:
            printing_and_logging(f'{self} collected {amount} from the the bank')
        else:
            printing_and_logging(f'{self} paid the bank an amount of {-amount}')


    def build_house(self, asset):
        """
        Build a house in a property if player has the color set and the property can be developed.
        :param asset: A property where house is being built
        """
        try:
            if check_can_build_house(self, asset):
                asset._houses += 1
                self.bank_transaction(-asset.building_cost)
                printing_and_logging(f'{self} built a house on {asset}')
            else:
                printing_and_logging(f'{self} cannot build a house on {asset}')
        except InvalidPropertyTypeError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotBuildHouseError(self, asset)
        except UnownedPropertyError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotBuildHouseError(self, asset)
        except PropertyNotFreeError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotBuildHouseError(self, asset)

    def build_hotel(self, asset):
        """
        Build hotel in property
        :param asset: The tile where the hotel is being built
        """
        try:
            if check_can_build_hotel(self, asset):
                asset._hotel = True
                self.bank_transaction(-asset.building_cost)
                printing_and_logging(f'{self} built a hotel on {asset}')
            else:
                printing_and_logging(f'{self} cannot build a hotel on {asset}')
        except InvalidPropertyTypeError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotBuildHotelError(self, asset)
        except UnownedPropertyError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotBuildHotelError(self, asset)
        except PropertyNotFreeError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotBuildHotelError(self, asset)

    def pay_jail_fine(self):
        """
        Pay fine to get out of jail
        """
        if self.cash > 50:
            self.bank_transaction(-50)
            self.in_jail = False
            printing_and_logging(f'{self} paid a fine and got out of jail')

    def try_jail_double_throw(self):
        """
        Try to throw a double to get out of jail. You get three turns to throw a double. After three turns, you pay the fine.
        """
        dice1 = self.throw_one_dice()
        printing_and_logging(f'dice 1: {dice1} ')
        dice2 = self.throw_one_dice()
        printing_and_logging(f'dice 2: {dice2} ')
        self.jail_throw_counter += 1
        if dice1 == dice2:
            self.in_jail = False
            printing_and_logging(f'{self} threw a double and got out of jail')
            self.move(dice1 + dice2)
            return dice1 + dice2
        else:
            printing_and_logging(f'{self} tried to throw a double but failed. Chances left: {3 - self.jail_throw_counter}')
        if self.jail_throw_counter == 3:
            self.pay_jail_fine()
            self.in_jail = False
            self.move(dice1 + dice2)
            self.jail_throw_counter = 0
            printing_and_logging(f'{self} used all of their three chances to throw a double.')
            return dice1 + dice2


    def get_out_of_jail_free(self):
        """
        Use get out of jail free card.
        """
        self.get_out_of_jail_free_card -= 1
        self.in_jail = False
        printing_and_logging(f'{self} used a Get Out of Jail Free card')

    def sell_house(self, asset):
        """
        Sell the house on a property
        :param asset: The asset with houses on it
        """
        try:
            if check_can_sell_house(self, asset):
                self.bank_transaction(asset._building_cost / 2)
                asset._houses -= 1
                printing_and_logging(f'{self} sold a house on {asset}')
            else:
                printing_and_logging(f'{self} cannot sell the house on {asset}')
        except InvalidPropertyTypeError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotSellHouseError(self, asset)
        except UnownedPropertyError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotSellHouseError(self, asset)
        except PropertyNotFreeError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotSellHouseError(self, asset)

    def sell_hotel(self, asset):
        """
        Sell the hotel on the property
        :param asset: The property with hotel it
        """
        try:
            if  check_can_sell_hotel(self, asset):
                self.bank_transaction(asset._building_cost / 2)
                asset._hotel = False
                printing_and_logging(f'{self} sold the hotel on {asset}')
            else:
                printing_and_logging(f'{self} cannot sell the hotel on {asset}')
        except InvalidPropertyTypeError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotSellHotelError(self, asset)
        except UnownedPropertyError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotSellHotelError(self, asset)
        except PropertyNotFreeError as e:
            logger.error(e.exc_message, exc_info=True)
            raise CannotSellHotelError(self, asset)

    def sell_all_hotels(self, color):
        """
        Sell hotels on all properties in the color set
        :param color: The color of the color set
        """
        property_list = [asset for asset in self.player_portfolio if (asset.color == color and type(asset) not in [Railroad, Utility])]
        for each_property in property_list:
                self.sell_hotel(each_property)

    def sell_all_houses(self, color):
        """
        Sell all houses on all properties in the color set
        :param color: The color of the color set
        """
        property_list = [asset for asset in self.player_portfolio if
                         (asset.color == color and type(asset) not in [Railroad, Utility])]
        for i in range(0, 4):
            for each_property in property_list:
                if each_property._houses != 0:
                    if not self.sell_house(each_property):
                        continue

    def mortgage_property(self, asset):
        """
        Mortgage a property. Receive the mortgage value of the property. Rent cannot be collected on mortgaged property.
        :param asset: The asset being mortgaged.
        """
        self.sell_all_hotels(asset.color)
        self.sell_all_houses(asset.color)
        self.bank_transaction(asset.cost / 2)
        asset.mortgaged = True
        printing_and_logging(f'{self} mortgaged {asset}')

    def unmortgage_property(self, asset):
        """
        Unmortgage a mortgaged property. Pay an additional 10% on top of the mortgage amount to unmortgage it. Rent can be collected once the property is unmortgaged.
        :param asset: The asset being unmortgaged.
        """
        unmortgage_amount = (asset.cost / 2) * 1.1
        self.bank_transaction(-unmortgage_amount)
        asset.mortgaged = False
        printing_and_logging(f'{self} unmortgaged {asset}')





