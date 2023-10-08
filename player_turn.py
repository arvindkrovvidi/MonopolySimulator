from random import randint

from Tiles.ChanceTile import ChanceTile
from Tiles.CommunityChestTile import CommunityChestTile
from Tiles.Property import Property
from Tiles.Railroad import Railroad
from Tiles.Utility import Utility
from utils import check_player_has_color_set


def play_turn(current_tile, player, throw):
    """
    Play turn after throwing the dice and moving to a tile.
    :param current_tile: Tile the player landed on after throwing dice
    :param player: Player playing the turn
    :param throw: The dice throw
    """
    if type(current_tile) == Property:
        play_turn_property(current_tile, player)
    elif type(current_tile) == Railroad:
        player_turn_railroad(current_tile, player)
    elif type(current_tile) == Utility:
        player_turn_utility(current_tile, player, throw)
    elif type(current_tile) == CommunityChestTile:
        card_no = randint(1, 16)
        CommunityChestTile.execute(player, card_no)
    elif type(current_tile) == ChanceTile:
        card_no = randint(1, 16)
        ChanceTile.execute(player, card_no, throw=throw)


def play_turn_property(current_tile, player):
    """
    Play turn if the player lands on a Property
    :param current_tile: Property
    :param player: Player playing the turn
    """
    if current_tile.owner is None:
        player.buy_property(current_tile)
    elif current_tile in player.player_portfolio and check_player_has_color_set(player, current_tile.color):
        player.build_house(current_tile)
    elif current_tile.owner != player:
        landlord = current_tile.owner
        player.pay_rent(landlord, current_tile.rent)

def player_turn_railroad(current_tile, player):
    """
    Play turn if the player lands on a Railroad
    :param current_tile: Railroad
    :param player: Player playing the turn
    """
    if current_tile.owner is None:
        player.buy_railroad(current_tile)
    else:
        landlord = current_tile.owner
        player.pay_rent(landlord, current_tile.rent[landlord.railroads_owned - 1])

def player_turn_utility(current_tile, player, throw):
    """
    Play turn if the player lands on a Utility
    :param current_tile: Utility
    :param player: Player playing the turn
    :param throw: The dice throw
    """
    if current_tile.owner is None:
        player.buy_utility(current_tile)
    else:
        landlord = current_tile.owner
        if check_player_has_color_set(landlord, "Utility"):
            player.pay_rent(landlord, throw * 10)
        else:
            player.pay_rent(landlord, throw * 4)