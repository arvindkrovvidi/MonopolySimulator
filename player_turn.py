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
from errors import InsufficientFundsError, PropertyNotFreeError, CannotBuildHotelError, CannotBuildHouseError, \
    CannotSellHouseError
from utils import check_player_has_color_set, check_can_buy_asset, check_can_build_house, check_can_build_hotel, \
    check_can_sell_hotel, check_can_sell_house, UnownedPropertyError


def play_turn(player, current_tile, throw=None):
    if type(current_tile) in [Property, Railroad, Utility]:
        available_options = get_available_options_properties(all_tiles_list[player.tile_no], player, throw)
        if available_options is None:
            return
        option_function_dict = dict(list(enumerate(available_options)))
        print(get_display_options(available_options))
        user_input = int(input(f'Select an option from the above: '))
        run_player_option(player, all_tiles_list[player.tile_no], option_function_dict, user_input)
    if type(current_tile) == ChanceTile:
        card_no = randint(1, 16)
        chance_return_value = current_tile.execute(player, card_no, throw=throw)
        if chance_return_value is not None:
            available_options = get_available_options_properties(all_tiles_list[player.tile_no], player, throw)
            option_function_dict = dict(list(enumerate(available_options)))
            get_display_options(available_options)
            user_input = int(input(f'Select an option from the above: '))
            run_player_option(player, all_tiles_list[player.tile_no], option_function_dict, user_input)
    if type(current_tile) == CommunityChestTile:
        card_no = randint(1, 16)
        current_tile.execute(player, card_no)
    elif type(current_tile) == LuxuryTaxTile or type(current_tile) == IncomeTaxTile:
        current_tile.execute(player)
    elif type(current_tile) in [Jail, GoToJail, LuxuryTaxTile, IncomeTaxTile, FreeParkingTile]:
        current_tile.execute(player)

def get_available_options_properties(current_tile, player, throw=None):
    """
    Play turn after throwing the dice and moving to a tile.
    :param current_tile: Tile the player landed on after throwing dice
    :param player: Player playing the turn
    :param throw: The dice throw
    """
    available_options = []
    if type(current_tile) == Property:
        available_options = play_turn_property(current_tile, player)
    elif type(current_tile) == Railroad:
        available_options = player_turn_railroad(current_tile, player)
    elif type(current_tile) == Utility:
        available_options = player_turn_utility(current_tile, player, throw)

    if available_options is None:
        return
    available_options.append('Do nothing')
    return available_options

def run_player_option(player, current_tile, option_function_dict, user_input):
    if option_function_dict[user_input] == 'Buy property':
        player.buy_asset(current_tile)
    elif option_function_dict[user_input] == 'Build house':
        player.build_house(current_tile)
    elif option_function_dict[user_input] == 'Build hotel':
        player.build_hotel(current_tile)
    elif option_function_dict[user_input] == 'Sell house':
        player.sell_house(current_tile)
    elif option_function_dict[user_input] == 'Sell hotel':
        player.sell_hotel(current_tile)
    elif option_function_dict[user_input] == 'Do nothing':
        print(f'{player} did nothing this turn')
        logger.info(f'{player} did nothing this turn')
        pass

def play_turn_property(current_tile, player):
    """
    Play turn if the player lands on a Property
    :param current_tile: Property
    :param player: Player playing the turn
    """
    available_options = []
    try:
        check_can_buy_asset(player, current_tile)
    except InsufficientFundsError as e:
        logger.info(e.exc_message)
    except PropertyNotFreeError as e:
        logger.info(e.exc_message)
        landlord = current_tile.owner
        player.pay_rent(landlord, current_tile.rent)
    else:
        available_options.append('Buy property')

    try:
        if check_can_build_house(player, current_tile):
            available_options.append('Build house')
    except CannotBuildHouseError as e:
        logger.info(e.exc_message)
    except UnownedPropertyError as e:
        logger.info(e.exc_message)
    except PropertyNotFreeError as e:
        logger.info(e.exc_message)

    try:
        if check_can_build_hotel(player, current_tile):
            available_options.append('Build hotel')
    except CannotBuildHotelError as e:
        logger.info(e.exc_message)
    except UnownedPropertyError as e:
        logger.info(e.exc_message)
    except PropertyNotFreeError as e:
        logger.info(e.exc_message)

    try:
        if check_can_sell_house(player, current_tile):
            available_options.append('Sell house')
    except CannotSellHouseError as e:
        logger.info(e.exc_message)
    except UnownedPropertyError as e:
        logger.info(e.exc_message)
    except PropertyNotFreeError as e:
        logger.info(e.exc_message)

    try:
        if check_can_sell_hotel(player, current_tile):
            available_options.append('Sell hotel')
    except CannotSellHouseError as e:
        logger.info(e.exc_message)
    except UnownedPropertyError as e:
        logger.info(e.exc_message)
    except PropertyNotFreeError as e:
        logger.info(e.exc_message)

    return available_options

def player_turn_railroad(current_tile, player):
    """
    Play turn if the player lands on a Railroad
    :param current_tile: Railroad
    :param player: Player playing the turn
    """
    available_options = []
    try:
        check_can_buy_asset(player, current_tile)
    except InsufficientFundsError as e:
        logger.info(e.exc_message)
    except PropertyNotFreeError as e:
        logger.info(e.exc_message)
        landlord = current_tile.owner
        player.pay_rent(landlord, current_tile.rent)
    else:
        available_options.append('Buy property')

    return available_options


def player_turn_utility(current_tile, player, throw):
    """
    Play turn if the player lands on a Utility
    :param current_tile: Utility
    :param player: Player playing the turn
    :param throw: The dice throw
    """
    available_options = []
    try:
        check_can_buy_asset(player, current_tile)
    except InsufficientFundsError as e:
        logger.info(e.exc_message)
    except PropertyNotFreeError as e:
        logger.info(e.exc_message)
        landlord = current_tile.owner
        if check_player_has_color_set(landlord, "Utility"):
            player.pay_rent(landlord, throw * 10)
        else:
            player.pay_rent(landlord, throw * 4)
    else:
        available_options.append('Buy property')
    return available_options