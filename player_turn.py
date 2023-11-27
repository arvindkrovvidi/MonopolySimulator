from random import randint

from Player_data import all_players_list
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
from Tiles_data.all_tiles_data import all_tiles_list
from config import printing_and_logging
from errors import InsufficientFundsError, PropertyNotFreeError, InvalidPropertyTypeError, SelfOwnedPropertyError
from utils import check_player_has_color_set, check_can_buy_asset, check_can_build_house, check_can_build_hotel, \
    check_can_sell_hotel, check_can_sell_house, get_display_options


def play_turn(player, current_tile, throw=None):
    if type(current_tile) in [Property, Railroad, Utility]:
        printing_and_logging(f'Property: {current_tile}    Cost: {current_tile.cost}')
        handle_player_input(player, current_tile, throw)
    elif type(current_tile) == ChanceTile:
        card_no = randint(1, 16)
        chance_return_value = current_tile.execute(player, card_no, all_players_list=all_players_list, throw=throw)
        if type(chance_return_value) is bool:
            handle_player_input(player, throw)
        elif chance_return_value == 4:
            all_tiles_list[chance_return_value].execute(player)
        elif chance_return_value == 19:
            handle_player_input(player, all_tiles_list[player.tile_no], throw)
        elif chance_return_value == 33:
            card_no = randint(1, 16)
            all_tiles_list[chance_return_value].execute(player, card_no, all_players_list=all_players_list)
    elif type(current_tile) == CommunityChestTile:
        card_no = randint(1, 16)
        current_tile.execute(player, card_no, all_players_list=all_players_list)
    elif type(current_tile) == LuxuryTaxTile or type(current_tile) == IncomeTaxTile:
        current_tile.execute(player)
    elif type(current_tile) in [LuxuryTaxTile, IncomeTaxTile, FreeParkingTile]:
        current_tile.execute(player)
    elif type(current_tile) == GoToJail:
        current_tile.execute(player)
    elif type(current_tile) == Jail:
        pass

def get_available_options_assets(current_tile, player, throw=None):
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
        available_options = play_turn_railroad(current_tile, player)
    elif type(current_tile) == Utility:
        available_options = play_turn_utility(current_tile, player, throw)

    available_options.append('End turn')
    return available_options

def run_player_option(player, current_tile, user_input_function):
    """
    Run the function corresponding to the option the player selects.
    """
    if user_input_function == 'Buy property':
        player.buy_asset(current_tile)
    elif user_input_function == 'Build house':
        player.build_house(current_tile)
    elif user_input_function == 'Build hotel':
        player.build_hotel(current_tile)
    elif user_input_function == 'Sell house':
        player.sell_house(current_tile)
    elif user_input_function == 'Sell hotel':
        player.sell_hotel(current_tile)
    elif user_input_function == 'End turn':
        printing_and_logging(f'{player} ended their turn')
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
        printing_and_logging(f'{player} cannot buy {current_tile}')
        printing_and_logging(e.exc_message)
    except PropertyNotFreeError:
        landlord = current_tile.owner
        player.pay_rent(landlord, current_tile.rent)
    except SelfOwnedPropertyError as e:
        printing_and_logging(e.exc_message)
        if check_can_build_house(player, current_tile):
            available_options.append('Build house')
        if check_can_build_hotel(player, current_tile):
            available_options.append('Build hotel')
        if check_can_sell_house(player, current_tile):
            available_options.append('Sell house')
        if check_can_sell_hotel(player, current_tile):
            available_options.append('Sell hotel')
    except InvalidPropertyTypeError as e:
        printing_and_logging(e.exc_message)
    else:
        available_options.append('Buy property')
    return available_options

def play_turn_railroad(current_tile, player):
    """
    Play turn if the player lands on a Railroad
    :param current_tile: Railroad
    :param player: Player playing the turn
    """
    available_options = []
    try:
        check_can_buy_asset(player, current_tile)
    except InsufficientFundsError as e:
        printing_and_logging(f'{player} cannot buy {current_tile}')
        printing_and_logging(e.exc_message)
    except PropertyNotFreeError as e:
        printing_and_logging(e.exc_message)
        landlord = current_tile.owner
        player.pay_rent(landlord, current_tile.rent)
    except SelfOwnedPropertyError as e:
        printing_and_logging(e.exc_message)
    else:
        available_options.append('Buy property')
    return available_options

def play_turn_utility(current_tile, player, throw):
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
        printing_and_logging(f'{player} cannot buy {current_tile}')
    except PropertyNotFreeError as e:
        printing_and_logging(e.exc_message)
        landlord = current_tile.owner
        if check_player_has_color_set(landlord, "Utility"):
            player.pay_rent(landlord, current_tile.get_rent(throw))
        else:
            player.pay_rent(landlord, current_tile.get_rent(throw))
    except SelfOwnedPropertyError as e:
        printing_and_logging(e.exc_message)
    else:
        available_options.append('Buy property')
    return available_options

def play_turn_jail(player):
    """
    Defines how to proceed if player is in jail at the beginning of their turn
    :param player: The player that is in jail.
    """
    current_tile = all_tiles_list[player.tile_no]
    printing_and_logging(f'{player} is in Jail')
    available_options = current_tile.get_available_options(player)
    print(get_display_options(available_options))
    player_option = int(input(f'Select an option from the above: '))
    jail_output = current_tile.execute(player, player_option)
    if jail_output == 'Paid fine':
        throw = player.throw_dice(ignore_double=True)
        player.move(throw)
        current_tile = all_tiles_list[player.tile_no]
        play_turn(player, current_tile, throw)
    elif type(jail_output) == int:
        player.move(jail_output)
        current_tile = all_tiles_list[player.tile_no]
        play_turn(player, current_tile, jail_output)

def throw_move_and_play_turn(player):
    throw = player.throw_dice()
    player.move(throw)
    current_tile = all_tiles_list[player.tile_no]
    play_turn(player, current_tile, throw)
    printing_and_logging(f'Player: {player}    Location: {all_tiles_list[player.tile_no]}    Cash: {player.cash}')

def handle_player_input(player, current_tile, throw=None):
    user_input_function = ''
    while user_input_function != 'End turn':
        available_options = get_available_options_assets(current_tile, player, throw)
        option_function_dict = dict(list(enumerate(available_options)))
        print(get_display_options(available_options))
        user_input_num = int(input(f'Select an option from the above: '))
        user_input_function = option_function_dict[user_input_num]
        run_player_option(player, current_tile, user_input_function)

def get_properties_for_building_houses(player):
    """
    Get list of properties  from the player's portfolio that are eligible for building houses.
    """
    eligible_properties_list = []
    for asset in player.player_portfolio:
        if type(asset) not in [Railroad, Utility]:
            if check_can_build_house_on_property(player, asset):
                eligible_properties_list.append(asset)
    return eligible_properties_list
