import inspect
from copy import deepcopy
from random import randint

from prettytable import PrettyTable

from Board import color_data
from Tiles.Property import Property
from Tiles.Tile import Tile
from config import printing_and_logging
from errors import InvalidPropertyTypeError, PropertyNotFreeError, InsufficientFundsError, UnownedPropertyError, \
    SelfOwnedPropertyError


def calculate_networth(player) -> int:
    """
    Calculate networth of a player
    :param player: Player who's networth is being calculated
    :return: Networth
    """
    nw = 0
    for asset in player.player_portfolio:
        nw += asset.cost
    nw += player.cash
    return nw


def find_winner(players):
    """
    Find the winner of the game based on networths
    :param players: List of all the players in the game
    :return: Winner and their index in the list
    """
    nw_list = [player.networth for player in players]
    max_nw = max(nw_list)
    winner_index = nw_list.index(max_nw)
    winner = players[winner_index]
    return winner, winner_index


def get_positions(players):
    """
    Generator that yields the position, winner and their networth
    :param players: List of all players in the game
    """
    j = 0
    for i in range(len(players)):
        winner, winner_index = find_winner(players)
        if i != 0:
            if prev.networth == winner.networth:
                yield i - j, winner, winner.networth
                j += 1
                prev = winner
            else:
                yield i + 1, winner, winner.networth
                prev = winner
                j -= 1
                if j < 0:
                    j = 0
        else:
            yield i + 1, winner, winner.networth
            prev = winner
        players.pop(winner_index)

def check_passing_go(player, tile: Tile) -> bool:
    """
    Check if moving to a tile requires crossing Go tile. This is required for Chance cards.
    :param player: Player that is moving to tile
    :param tile: The tile that the player is moving to.
    :return: True if passing Go else False.
    """
    if player.tile_no < tile.tile_no:
        return False
    else:
        return True

def check_can_buy_asset(player, asset):
    """
    Check if player can buy the asset.
    :param player: Player trying to buy the asset
    :param asset: Property, Railroad or utility
    :return: True if the player can buy the asset. Else False.
    """
    if asset.owner not in [None, player]:
        raise PropertyNotFreeError(asset)
    elif asset.cost > player.cash:
        raise InsufficientFundsError(player)
    elif asset.owner is player:
        raise SelfOwnedPropertyError(player, asset)
    return True

def check_player_has_color_set(player, color):
    """
    Check if the player has all the properties in the color set.
    :param player: The player who is being tested for owning the color set.
    :param color: The color which is being tested.
    :return: True if the player has the color set. False if they do not.
    """
    count = 0
    for each_property in player.player_portfolio:
        if each_property.color == color:
            count += 1
    if count == color_data[color]:
        return True
    return False

def check_can_build_house_on_property(player, asset):
    """
    Check if a house can be built on the property.
    :param player: The player trying to build the house
    :param asset: Property
    :return: True if the player has the cash, the color set and the asset does not already have the most houses among the assets in the color set.
    """
    if type(asset) is not Property:
        raise InvalidPropertyTypeError(inspect.stack()[0][3], asset)
    elif asset.owner is None:
        raise UnownedPropertyError(asset)
    elif asset.owner is not player:
        raise PropertyNotFreeError(asset)
    elif asset.building_cost > player.cash:
        return False
    elif not check_player_has_color_set(player,asset.color):
        return False
    elif asset._houses == 4:
        return False
    for each_property in asset.owner.player_portfolio:
        if each_property.color != asset.color:
            continue
        if each_property == asset:
            continue
        if asset._houses > each_property._houses:
            return False
    return True

def check_can_build_hotel_on_property(player, asset):
    """
    Check if a hotel can be built on the given property. A hotel can be built only if all the properties in the color set have 4 houses each.
    :param player: The player trying to build the hotel
    :param asset: The asset being tested if there can be a hotel built
    :return: True if all the properties in the color set have 4 houses. False if even one property does not have 4 houses.
    """
    if type(asset) is not Property:
        raise InvalidPropertyTypeError(inspect.stack()[0][3], asset)
    elif asset.owner is None:
        raise UnownedPropertyError(asset)
    elif asset.owner is not player:
        raise PropertyNotFreeError(asset)
    elif asset._hotel:
        return False
    elif player.cash < asset.building_cost:
        return False
    for each_property in asset.owner.player_portfolio:
        if each_property.color != asset.color:
            continue
        if each_property._houses != 4:
            return False
    return True

def check_can_sell_house_on_property(player, asset):
    """
    Check whether a house on this property can be sold
    :param player: The player trying to sell the house
    :param asset: Property
    """
    if type(asset) is not Property:
        raise InvalidPropertyTypeError(inspect.stack()[0][3], asset)
    elif asset.owner is None:
        raise UnownedPropertyError(asset)
    elif asset.owner is not player:
        raise PropertyNotFreeError(asset)
    elif asset._hotel == True:
        return False
    elif asset._houses <= 0:
        return False
    for each_property in asset.owner.player_portfolio:
        if each_property.color != asset.color:
            continue
        if each_property == asset:
            continue
        if asset._houses < each_property._houses:
            return False
    return True

def check_can_sell_hotel_on_property(player, asset):
    """
    Check whether the hotel on this property can be sold.
    :param player: The player trying to see the hotel
    :param asset:
    """
    if type(asset) is not Property:
        raise InvalidPropertyTypeError(inspect.stack()[0][3], asset)
    elif asset.owner is None:
        raise UnownedPropertyError(asset)
    elif asset.owner is not player:
        raise PropertyNotFreeError(asset)
    elif asset._hotel == True:
        return True
    return False

def check_can_mortgage_asset(asset):
    """
    Check whether the property can be mortgaged
    """
    # if asset.owner is None:
    #     raise UnownedPropertyError(asset)
    if not asset._hotel:
        return False
    if asset._houses != 0:
        return False
    return True

def check_can_unmortgage_asset(player, asset):
    """
    Check whether the property can be unmortgaged
    """
    # if asset.owner is None:
    #     return False
    # elif asset.owner is not player:
    #     return False
    if player.cash < asset.unmortgage_cost:
        return False
    return True

def check_any_player_broke(player_list):
    """
    Check if a player has cash less than 0
    :param player_list: List of all players
    :return: True if a player has cash less than 0. Else False.
    """
    for player in player_list:
        if player.cash < 0:
            return True
    return False

def print_player_summary(players):
    """
    Print player summary with Position, player and their networth.
    :param players_copy: List of all players
    """
    players_copy = deepcopy(players)
    for player in players_copy:
        player.networth = calculate_networth(player)

    display_winners = PrettyTable()
    display_winners.field_names = ["Position", "Player", "Net Worth"]
    for pos, win, nw in get_positions(players_copy):
        display_winners.add_row((pos, str(win), nw))
    printing_and_logging(display_winners)

def set_color_set_value(player, asset):
    """
    Set the color_set value for all properties once a player buys the last property in the set.
    :param player: Player that completes the color set.
    :param asset: The last property in the set that the player bought.
    """
    if type(asset) is not Property:
        raise InvalidPropertyTypeError(inspect.stack()[0][3], asset)
    for each_property in player.player_portfolio:
        if each_property.color == asset.color:
            each_property._color_set = True

def randomly_play_jail_turn(player):
    """
    Choose whether the player pays jail fine or tries for a double randomly.
    :param player:
    """
    num = randint(1, 2)
    if num == 1:
        player.pay_jail_fine()
    elif num == 2:
        player.try_jail_double_throw()

def get_display_options(*args):
    """
    Display the options that are passed to the function
    :param args: List of options
    :return: String in the format [s.no] <option>
    """
    options_string = ''
    for option in args[0]:
         options_string += f'[{args[0].index(option)}] {str(option)}' + '    '
    return options_string

def get_player_input(text, available_options):
    """
    Get input from player
    :param text: Text to be displayed while collecting input. This is passed to the python input() function
    :param available_options: List of possible options
    :return: The input given by the player
    """
    while True:
        try:
            player_input = int(input(text + ': '))
            if player_input not in available_options:
                raise ValueError
        except ValueError:
            print('Invalid input')
            continue
        else:
            return player_input

def display_assets(player):
    """
    Display the list of properties owned by a player
    :param player:
    """
    assets_table = PrettyTable()
    assets_table.field_names = ['S.No', 'Property', 'Cost', 'Houses', 'Hotel', 'Status']

    for no, each_asset in enumerate(player.player_portfolio, start=1):
        if type(each_asset) == Property:
            assets_table.add_row([no, str(each_asset), each_asset.cost, each_asset._houses, 'Yes' if each_asset._hotel else 'No', 'Mortgaged' if each_asset.mortgaged else 'Active'])
        else:
            assets_table.add_row([no, str(each_asset), each_asset.cost, '-', '-', 'Mortgaged' if each_asset.mortgaged else 'Active'])
    print(assets_table)
