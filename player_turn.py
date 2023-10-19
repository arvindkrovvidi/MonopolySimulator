from random import randint

from Tiles.ChanceTile import ChanceTile
from Tiles.CommunityChestTile import CommunityChestTile
from Tiles.FreeParkingTile import FreeParkingTile
from Tiles.GoToJail import GoToJail
from Tiles.IncomeTaxTile import IncomeTaxTile
from Tiles.Jail import Jail
from Tiles.LuxuryTaxTile import LuxuryTaxTile
from Tiles.Property import Property
from Tiles.Railroad import Railroad
from Tiles.Utility import Utility
from config import logger
from errors import InsufficientFundsError, PropertyNotFreeError, CannotBuildHotelError, CannotBuildHouseError
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
        current_tile.execute(player, card_no)
    elif type(current_tile) == ChanceTile:
        card_no = randint(1, 16)
        current_tile.execute(player, card_no, throw=throw)
    elif type(current_tile) == LuxuryTaxTile or type(current_tile) == IncomeTaxTile:
        current_tile.execute(player)
    elif type(current_tile) in [Jail, GoToJail, LuxuryTaxTile, IncomeTaxTile, FreeParkingTile]:
        current_tile.execute(player)

def play_turn_property(current_tile, player):
    """
    Play turn if the player lands on a Property
    :param current_tile: Property
    :param player: Player playing the turn
    """
    try:
        player.buy_asset(current_tile)
    except InsufficientFundsError as e:
        logger.info(e.exc_message)
    except PropertyNotFreeError as e:
        logger.info(e.exc_message)
        landlord = current_tile.owner
        player.pay_rent(landlord, current_tile.rent)
    else:
        try:
            player.build_house(current_tile)
        except CannotBuildHouseError as e:
            logger.info(e.exc_message)
        except CannotBuildHotelError as e:
            logger.info(e.exc_message)

def player_turn_railroad(current_tile, player):
    """
    Play turn if the player lands on a Railroad
    :param current_tile: Railroad
    :param player: Player playing the turn
    """
    try:
        player.buy_asset(current_tile)
    except InsufficientFundsError as e:
        logger.info(e.exc_message)
    except PropertyNotFreeError as e:
        logger.info(e.exc_message)
        landlord = current_tile.owner
        player.pay_rent(landlord, current_tile.rent)

def player_turn_utility(current_tile, player, throw):
    """
    Play turn if the player lands on a Utility
    :param current_tile: Utility
    :param player: Player playing the turn
    :param throw: The dice throw
    """
    try:
        player.buy_asset(current_tile)
    except InsufficientFundsError:
        logger.info(f'{player} does not have cash to buy {current_tile}')
    except PropertyNotFreeError:
        logger.info(f'{current_tile} already owned by {current_tile.owner}')
        landlord = current_tile.owner
        if check_player_has_color_set(landlord, "Utility"):
            player.pay_rent(landlord, throw * 10)
        else:
            player.pay_rent(landlord, throw * 4)