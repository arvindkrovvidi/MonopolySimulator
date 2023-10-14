import copy

from prettytable import PrettyTable

from Board import color_data
from Tiles.Property import Property
from Tiles.Railroad import Railroad
from Tiles.Tile import Tile
from Tiles_data.Property_data import property_data_by_color
from errors import InvalidPropertyTypeError


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

def get_railroads_owned(player):
    count = 0
    for asset in player.player_portfolio:
        if type(asset) == Railroad:
            count += 1

    return count

def check_property_can_be_developed(asset):
    """
    A house can be built in a property only if the property had the same number of houses as or less number of houses than the other properties in the color set.
    :param asset: The asset being tested for development
    :return: True if the property can be developed. False if the propert cannot be developed.
    """
    data = copy.deepcopy(property_data_by_color)
    asset_to_be_removed = data[asset.color][asset]
    data[asset.color].remove(asset_to_be_removed)
    remaining_list = data[asset.color]
    for each in remaining_list:
        if asset._houses > each._houses:
            return False
    return True

def check_can_build_hotel(asset):
    """
    Check if a hotel can be built on the given property. A hotel can be built only if all the properties in the color set have 4 houses each.
    :param asset: The asset being tested if there can be a hotel built
    :return: True if all the properties in the color set have 4 houses. False if even one property does not have 4 houses.
    """
    data = copy.deepcopy(property_data_by_color)
    for each_property in data[asset.color]:
        if each_property._houses < 4:
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
    for player in players:
        player.networth = calculate_networth(player)

    display_winners = PrettyTable()
    display_winners.field_names = ["Position", "Player", "Net Worth"]
    for pos, win, nw in get_positions(players):
        display_winners.add_row((pos, str(win), nw))
    print(display_winners)

def set_color_set_value(player, asset):
    if type(asset) is not Property:
        raise InvalidPropertyTypeError(set_color_set_value.__name__, asset)
    for each_property in player.player_portfolio:
        if each_property.color == asset.color:
            each_property._color_set = True
