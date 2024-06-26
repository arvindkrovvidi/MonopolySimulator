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
from utils import check_player_has_color_set, check_can_buy_asset, check_can_build_house_on_property, \
    check_can_build_hotel_on_property, \
    check_can_sell_hotel_on_property, check_can_sell_house_on_property, get_display_options, get_player_input, \
    display_assets


def play_turn(player, current_tile, throw=None):
    if type(current_tile) == ChanceTile:
        card_no = randint(1, 16)
        chance_return_value = current_tile.execute(player, card_no, all_players_list=all_players_list, throw=throw)
        if type(chance_return_value) is bool:
            get_available_options_and_player_input(player, player.current_tile, throw)
        elif chance_return_value == 4:
            all_tiles_list[chance_return_value].execute(player)
            get_available_options_and_player_input(player, player.current_tile, throw)
        elif chance_return_value == 19:
            get_available_options_and_player_input(player, player.current_tile, throw)
        elif chance_return_value == 33:
            card_no = randint(1, 16)
            all_tiles_list[chance_return_value].execute(player, card_no, all_players_list=all_players_list)
            get_available_options_and_player_input(player, player.current_tile, throw)
        elif chance_return_value is None:
            get_available_options_and_player_input(player, player.current_tile, throw)
    elif type(current_tile) == CommunityChestTile:
        card_no = randint(1, 16)
        current_tile.execute(player, card_no, all_players_list=all_players_list)
        get_available_options_and_player_input(player, player.current_tile, throw)
    elif type(current_tile) in [LuxuryTaxTile, IncomeTaxTile, FreeParkingTile]:
        current_tile.execute(player)
        get_available_options_and_player_input(player, current_tile, throw)
    elif type(current_tile) == GoToJail:
        current_tile.execute(player)
        get_available_options_and_player_input(player, current_tile, throw)
    elif type(current_tile) == Jail:
        get_available_options_and_player_input(player, player.current_tile, throw)
    elif type(current_tile) in [Property, Railroad, Utility]:
        printing_and_logging(f'Property: {current_tile}    Cost: {current_tile.cost}')
        get_available_options_and_player_input(player, current_tile, throw)


def get_available_options_assets(current_tile, player, throw=None):
    """
    Play turn after throwing the dice and moving to a tile.
    :param current_tile: Tile the player landed on after throwing dice
    :param player: Player playing the turn
    :param throw: The dice throw
    """
    available_options = ['End turn', 'Check portfolio']
    if type(current_tile) in [Property, Railroad, Utility]:
        try:
            check_can_buy_asset(player, current_tile)
        except PropertyNotFreeError:
            if type(current_tile) in [Property, Railroad]:
                landlord = current_tile.owner
                player.pay_rent(landlord, current_tile.rent)
            elif type(current_tile) == Utility:
                landlord = current_tile.owner
                if check_player_has_color_set(landlord, "Utility"):
                    player.pay_rent(landlord, current_tile.get_rent(throw))
                else:
                    player.pay_rent(landlord, current_tile.get_rent(throw))
        except InsufficientFundsError as e:
            printing_and_logging(f'{player} cannot buy {current_tile}')
            printing_and_logging(e.exc_message)
        except SelfOwnedPropertyError as e:
            printing_and_logging(e.exc_message)
        except InvalidPropertyTypeError as e:
            printing_and_logging(e.exc_message)
        else:
            available_options.append('Buy property')
        finally:
            if len(get_properties_for_building_houses(player)) != 0:
                available_options.append('Build house')
            if len(get_properties_for_selling_houses(player)) != 0:
                available_options.append('Sell house')
            if len(get_properties_for_building_hotels(player)) != 0:
                available_options.append('Build hotel')
            if len(get_properties_for_selling_hotels(player)) != 0:
                available_options.append('Sell hotel')
            if len(get_properties_for_mortgaging(player)) != 0:
                available_options.append('Mortgage asset')
            if len(get_properties_for_unmortgaging(player)) != 0:
                available_options.append('Unmortgage asset')
        return available_options
    else:
        if len(get_properties_for_building_houses(player)) != 0:
            available_options.append('Build house')
        if len(get_properties_for_selling_houses(player)) != 0:
            available_options.append('Sell house')
        if len(get_properties_for_building_hotels(player)) != 0:
            available_options.append('Build hotel')
        if len(get_properties_for_selling_hotels(player)) != 0:
            available_options.append('Sell hotel')
        if len(get_properties_for_mortgaging(player)) != 0:
            available_options.append('Mortgage asset')
        if len(get_properties_for_unmortgaging(player)) != 0:
            available_options.append('Unmortgage asset')
    return available_options

def run_player_option(player, current_tile, user_input_function):
    """
    Run the function corresponding to the option the player selects.
    """
    if user_input_function == 'Buy property':
        player.buy_asset(current_tile)
    elif user_input_function == 'Build house':
        eligible_properties = get_properties_for_building_houses(player)
        print(get_display_options(eligible_properties))
        player_choice_property = get_player_input('Select the property to build house', dict(enumerate(eligible_properties)).keys())
        player.build_house(eligible_properties[player_choice_property])
    elif user_input_function == 'Build hotel':
        eligible_properties = get_properties_for_building_hotels(player)
        print(get_display_options(eligible_properties))
        player_choice_property = get_player_input('Select the property to build hotel', dict(enumerate(eligible_properties)).keys())
        player.build_hotel(eligible_properties[player_choice_property])
    elif user_input_function == 'Sell house':
        eligible_properties = get_properties_for_selling_houses(player)
        print(get_display_options(eligible_properties))
        player_choice_property = get_player_input('Select the property to sell house', dict(enumerate(eligible_properties)).keys())
        player.sell_house(eligible_properties[player_choice_property])
    elif user_input_function == 'Sell hotel':
        eligible_properties = get_properties_for_selling_hotels(player)
        print(get_display_options(eligible_properties))
        player_choice_property = get_player_input('Select the property to sell house', dict(enumerate(eligible_properties)).keys())
        player.sell_hotel(eligible_properties[player_choice_property])
    elif user_input_function == 'Mortgage asset':
        eligible_assets = get_properties_for_mortgaging(player)
        print(get_display_options(eligible_assets))
        player_choice_asset = get_player_input('Select the asset to mortgage', dict(enumerate(eligible_assets)).keys())
        player.mortgage_property(eligible_assets[player_choice_asset])
    elif user_input_function == 'Unmortgage asset':
        eligible_assets = get_properties_for_unmortgaging(player)
        print(get_display_options(eligible_assets))
        player_choice_asset = get_player_input('Select the asset to unmortgage', dict(enumerate(eligible_assets)).keys())
        player.unmortgage_property(eligible_assets[player_choice_asset])
    elif user_input_function == 'Check portfolio':
        display_assets(player)
    elif user_input_function == 'End turn':
        printing_and_logging(f'{player} ended their turn')
        pass

def play_turn_jail(player):
    """
    Defines how to proceed if player is in jail at the beginning of their turn
    :param player: The player that is in jail.
    """
    current_tile = all_tiles_list[player.tile_no]
    printing_and_logging(f'{player} is in Jail')
    available_options = current_tile.get_available_options(player)
    available_options_dict = dict(enumerate(available_options))
    print(get_display_options(available_options))
    player_option = get_player_input('Select an option from the above', available_options_dict.keys())
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
    """
    Throw dice, move player and play turn
    """
    throw = player.throw_dice()
    player.move(throw)
    current_tile = all_tiles_list[player.tile_no]
    play_turn(player, current_tile, throw)
    printing_and_logging(f'Player: {player}    Location: {all_tiles_list[player.tile_no]}    Cash: {player.cash}')

def get_available_options_and_player_input(player, current_tile, throw=None):
    """
    Function to get available options, display the options and then run the corresponding function.
    """
    user_input_function = ''
    while user_input_function != 'End turn':
        asset_available_options = get_available_options_assets(current_tile, player, throw)
        option_function_dict = dict(list(enumerate(asset_available_options)))
        print(get_display_options(asset_available_options))
        user_input_num = get_player_input('Select an option from the above', option_function_dict.keys())
        user_input_function = option_function_dict[user_input_num]
        run_player_option(player, current_tile, user_input_function)

def get_properties_for_building_houses(player):
    """
    Get list of properties from the player's portfolio that are eligible for building houses.
    """
    eligible_properties_list = []
    for asset in player.player_portfolio:
        if type(asset) not in [Railroad, Utility]:
            if check_can_build_house_on_property(player, asset):
                eligible_properties_list.append(asset)
    return eligible_properties_list

def get_properties_for_selling_houses(player):
    """
    Get list of properties from the player's portfolio that are eligible for selling houses.
    """
    eligible_properties_list = []
    for asset in player.player_portfolio:
        if type(asset) not in [Railroad, Utility]:
            if check_can_sell_house_on_property(player, asset):
                eligible_properties_list.append(asset)
    return eligible_properties_list

def get_properties_for_building_hotels(player):
    """
    Get list of properties  from the player's portfolio that are eligible for building hotels.
    """
    eligible_properties_list = []
    for asset in player.player_portfolio:
        if type(asset) not in [Railroad, Utility]:
            if check_can_build_hotel_on_property(player, asset):
                eligible_properties_list.append(asset)
    return eligible_properties_list

def get_properties_for_selling_hotels(player):
    """
    Get list of properties  from the player's portfolio that are eligible for selling hotels.
    """
    eligible_properties_list = []
    for asset in player.player_portfolio:
        if type(asset) not in [Railroad, Utility]:
            if check_can_sell_hotel_on_property(player, asset):
                eligible_properties_list.append(asset)
    return eligible_properties_list

def get_properties_for_mortgaging(player):
    """
    Get list of properties from the player's portfolio that can be mortgaged
    :param player:
    """
    return [asset for asset in player.player_portfolio if not asset.mortgaged]

def get_properties_for_unmortgaging(player):
    """
    Get list of properties from the player's portfolio that can be mortgaged
    :param player:
    """
    return [asset for asset in player.player_portfolio if asset.mortgaged]
