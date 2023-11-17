import pytest

from player_turn import run_player_option, get_available_options_properties, play_turn_jail, play_turn_property, \
    play_turn_railroad
from tests.common import build_houses, build_all_hotels, buy_color_set


@pytest.mark.parametrize("asset", ["st_charles_place", "pennsylvania_railroad", "electric_company"])
@pytest.mark.parametrize("option", [0])
def test_run_player_option_buy_asset(arvind, st_charles_place, pennsylvania_railroad, electric_company, option, request,
                                     asset):
    """
    Test run_player_option for buy_property
    """
    option_function_dict = {0: 'Buy property', 1: 'End turn'}
    asset = request.getfixturevalue(asset)
    run_player_option(arvind, asset, option_function_dict, option)

    assert asset.owner == arvind
    assert asset in arvind.player_portfolio


def test_run_player_option_build_house(arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for build_house
    """
    arvind.cash = 1000
    option_function_dict = {0: 'Build house', 1: 'End turn'}
    arvind.buy_asset(st_charles_place)
    arvind.buy_asset(virginia_avenue)
    arvind.buy_asset(states_avenue)
    run_player_option(arvind, st_charles_place, option_function_dict, 0)

    assert st_charles_place._houses == 1


def test_run_player_option_build_hotel(arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for build_hotel
    """
    arvind.cash = 2000
    option_function_dict = {0: 'Build hotel', 1: 'End turn'}
    build_houses(arvind, [st_charles_place, virginia_avenue, states_avenue], 4)
    run_player_option(arvind, states_avenue, option_function_dict, 0)

    assert states_avenue._hotel == True


def test_run_player_option_sell_house(arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for sell_house
    """
    arvind.cash = 2000
    option_function_dict = {0: 'Sell house', 1: 'End turn'}
    buy_color_set(arvind, [st_charles_place, states_avenue, virginia_avenue])
    arvind.build_house(states_avenue)
    assert states_avenue._houses == 1
    run_player_option(arvind, states_avenue, option_function_dict, 0)
    assert states_avenue._houses == 0


def test_run_player_option_sell_hotel(arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for sell_hotel
    """
    arvind.cash = 2000
    option_function_dict = {0: 'Sell hotel', 1: 'End turn'}
    build_houses(arvind, [st_charles_place, states_avenue, virginia_avenue], 4)
    arvind.build_hotel(states_avenue)
    assert states_avenue._hotel == True
    run_player_option(arvind, states_avenue, option_function_dict, 0)

    assert states_avenue._hotel == False


def test_get_available_options_properties_1(arvind, states_avenue):
    """
    Test the available_options list when player lands on a free asset
    """
    arvind.move_to(states_avenue.tile_no, collect_go_cash_flag=False)
    current_tile = states_avenue
    available_options = get_available_options_properties(current_tile, arvind)
    assert 'Buy property' in available_options
    assert 'Build house' not in available_options
    assert 'Build hotel' not in available_options
    assert 'Sell house' not in available_options
    assert 'Sell hotel' not in available_options
    assert 'End turn' in available_options


def test_get_available_options_properties_2(arvind, states_avenue):
    """
    Test the available_options list when player lands on an asset owned by him but with no color set
    """
    arvind.move_to(states_avenue.tile_no, collect_go_cash_flag=False)
    current_tile = states_avenue
    arvind.buy_asset(states_avenue)
    available_options = get_available_options_properties(current_tile, arvind)
    assert 'Buy property' not in available_options
    assert 'Build house' not in available_options
    assert 'Build hotel' not in available_options
    assert 'Sell house' not in available_options
    assert 'Sell hotel' not in available_options
    assert 'End turn' in available_options


def test_get_available_options_properties_3(arvind, states_avenue, st_charles_place, virginia_avenue):
    """
    Test the available_options list when player lands on an asset owned by them, and they have the color set
    """
    arvind.cash = 1500
    arvind.move_to(states_avenue.tile_no, collect_go_cash_flag=False)
    current_tile = states_avenue
    buy_color_set(arvind, [st_charles_place, states_avenue, virginia_avenue])

    available_options = get_available_options_properties(current_tile, arvind)
    assert 'Buy property' not in available_options
    assert 'Build house' in available_options
    assert 'Build hotel' not in available_options
    assert 'Sell house' not in available_options
    assert 'Sell hotel' not in available_options
    assert 'End turn' in available_options


def test_get_available_options_properties_4(arvind, states_avenue, st_charles_place, virginia_avenue):
    """
    Test the available_options list when player lands on an asset owned by them, and they have 4 houses in all the properties in the color set.
    """
    arvind.cash = 2000
    arvind.move_to(states_avenue.tile_no, collect_go_cash_flag=False)
    current_tile = states_avenue
    build_houses(arvind, [st_charles_place, states_avenue, virginia_avenue], 4)
    available_options = get_available_options_properties(current_tile, arvind)
    assert 'Buy property' not in available_options
    assert 'Build house' not in available_options
    assert 'Build hotel' in available_options
    assert 'Sell house' in available_options
    assert 'Sell hotel' not in available_options
    assert 'End turn' in available_options


def test_get_available_options_properties_5(arvind, states_avenue, st_charles_place, virginia_avenue):
    """
    Test the available_options list when player lands on an asset owned by them, and they have hotels in all the properties in the color set.
    """
    arvind.cash = 2000
    arvind.move_to(states_avenue.tile_no, collect_go_cash_flag=False)
    current_tile = states_avenue
    build_all_hotels(arvind, [st_charles_place, states_avenue, virginia_avenue])
    available_options = get_available_options_properties(current_tile, arvind)
    assert 'Buy property' not in available_options
    assert 'Build house' not in available_options
    assert 'Build hotel' not in available_options
    assert 'Sell house' not in available_options
    assert 'Sell hotel' in available_options
    assert 'End turn' in available_options


def test_play_turn_jail_1(mocker, arvind, states_avenue):
    """
    Test play_turn_jail when the player chooses to pay the fine
    """
    arvind.move_to(10, collect_go_cash_flag=False)
    mocker.patch('player_turn.input', return_value='0')
    mocker.patch.object(arvind, 'throw_dice', return_value=3)
    play_turn_jail(arvind)
    assert arvind.cash == 10
    assert arvind.in_jail == False
    assert arvind.tile_no == 13
    assert states_avenue in arvind.player_portfolio


def test_play_turn_jail_2(mocker, arvind, virginia_avenue):
    """
    Test play_turn_jail when the player chooses to try double throw and throws a double
    """
    arvind.cash = 500
    arvind.move_to(10, collect_go_cash_flag=False)
    mocker.patch('player_turn.input', side_effect=['1', '0'])
    mocker.patch.object(arvind, 'throw_one_dice', return_value=2)
    mocker.patch.object(arvind, 'throw_dice', return_value=2)
    play_turn_jail(arvind)

    assert arvind.cash == 340
    assert arvind.in_jail == False
    assert arvind.tile_no == 14
    assert virginia_avenue in arvind.player_portfolio


def test_play_turn_jail_3(mocker, arvind):
    """
    Test play_turn_jail when the player chooses to try double throw and does not throw a double
    """
    arvind.cash = 500
    arvind.move_to(10, collect_go_cash_flag=False)
    mocker.patch('player_turn.input', return_value='1')
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[2, 3])
    play_turn_jail(arvind)

    assert arvind.in_jail == True
    assert arvind.cash == 500
    assert arvind.tile_no == 10


def test_play_turn_jail_4(mocker, arvind, pennsylvania_railroad):
    """
    Test play_turn_jail when the player fails to throw doubles three times
    """
    arvind.cash = 500
    arvind.move_to(10, collect_go_cash_flag=False)
    mocker.patch('player_turn.input', side_effect=['1', '1', '1', '0'])
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[2, 3, 2, 3, 2, 3])

    play_turn_jail(arvind)
    play_turn_jail(arvind)
    play_turn_jail(arvind)

    assert arvind.cash == 250
    assert arvind.in_jail == False
    assert arvind.tile_no == 15
    assert pennsylvania_railroad in arvind.player_portfolio


def test_play_turn_jail_5(mocker, arvind, pennsylvania_railroad):
    """
    Test play_turn_jail when the player fails to throw double in first try and pays fine in second try.
    """
    arvind.cash = 500
    arvind.move_to(10, collect_go_cash_flag=False)
    mocker.patch('player_turn.input', side_effect=['1', '0', '0'])
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[2, 3, 2, 3])

    play_turn_jail(arvind)
    play_turn_jail(arvind)

    assert arvind.cash == 250
    assert arvind.in_jail == False
    assert arvind.tile_no == 15
    assert pennsylvania_railroad in arvind.player_portfolio


def test_play_turn_jail_6(mocker, arvind, pennsylvania_railroad):
    """
    Test play_turn_jail when the player uses get out of jail free card.
    """
    arvind.get_out_of_jail_free_card = 1
    arvind.cash = 500
    arvind.move_to(10, collect_go_cash_flag=False)
    mocker.patch('player_turn.input', side_effect=['2', '0'])
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[2, 3])

    play_turn_jail(arvind)

    assert arvind.cash == 300
    assert arvind.in_jail == False
    assert arvind.tile_no == 15
    assert pennsylvania_railroad in arvind.player_portfolio


def test_play_turn_property_1(arvind, states_avenue):
    """
    Test play_turn_property when the property is free.
    """

    assert play_turn_property(states_avenue, arvind) == ['Buy property']
    assert arvind.cash == 200

def test_play_turn_property_2(arvind, states_avenue):
    """
    Test play_turn_property when the player already owns the property.
    """

    arvind.buy_asset(states_avenue)
    assert play_turn_property(states_avenue, arvind) == []
    assert arvind.cash == 60

def test_play_turn_property_3(arvind, states_avenue, arun):
    """
    Test play_turn_property when another player owns the property.
    """

    arun.buy_asset(states_avenue)
    assert play_turn_property(states_avenue, arvind) == []
    assert arvind.cash == 190
    assert arun.cash == 70
    assert states_avenue in arun.player_portfolio

def test_play_turn_property_4(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_property when the player owns the color set.
    """
    arvind.cash = 2000

    buy_color_set(arvind, [states_avenue, virginia_avenue, st_charles_place])
    assert play_turn_property(states_avenue, arvind) == ['Build house']

def test_play_turn_property_5(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_property when the player has less than 4 houses on any property.
    """
    arvind.cash = 2000

    build_houses(arvind, [states_avenue, virginia_avenue, st_charles_place], 3)
    assert play_turn_property(states_avenue, arvind) == ['Build house', 'Sell house']

def test_play_turn_property_6(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_property when the player has 4 houses on all properties.
    """
    arvind.cash = 2000

    build_houses(arvind, [states_avenue, virginia_avenue, st_charles_place], 4)
    assert play_turn_property(states_avenue, arvind) == ['Build hotel', 'Sell house']

def test_play_turn_property_7(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_property when the player has a hotel on the property.
    """
    arvind.cash = 2000

    build_houses(arvind, [states_avenue, virginia_avenue, st_charles_place], 4)
    arvind.build_hotel(states_avenue)
    assert play_turn_property(states_avenue, arvind) == ['Sell hotel']

def test_play_turn_property_8(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_property when the player has a hotel on a different property in the same color set.
    """
    arvind.cash = 2000

    build_houses(arvind, [states_avenue, virginia_avenue, st_charles_place], 4)
    arvind.build_hotel(virginia_avenue)
    assert play_turn_property(states_avenue, arvind) == ['Build hotel', 'Sell house']

def test_play_turn_property_9(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_property when the player has a hotel on all the properties in the color set.
    """
    arvind.cash = 2000

    build_all_hotels(arvind, [states_avenue, virginia_avenue, st_charles_place])
    assert play_turn_property(states_avenue, arvind) == ['Sell hotel']

def test_play_turn_railroad_1(arvind, pennsylvania_railroad):
    """
    Test play_turn_property when the railroad is free.
    """

    assert play_turn_railroad(pennsylvania_railroad, arvind) == ['Buy property']
    assert arvind.cash == 200

def test_play_turn_railroad_2(arvind, pennsylvania_railroad):
    """
    Test play_turn_property when the player already owns the railroad.
    """
    arvind.buy_asset(pennsylvania_railroad)
    assert play_turn_railroad(pennsylvania_railroad, arvind) == []
    assert arvind.cash == 0

def test_play_turn_railroad_3(arvind, arun, pennsylvania_railroad):
    """
    Test play_turn_property when another player already owns the railroad.
    """
    arun.buy_asset(pennsylvania_railroad)

    assert play_turn_railroad(pennsylvania_railroad, arvind) == []
    assert arvind.cash == 175
    assert arun.cash == 25

def test_play_turn_railroad_4(arvind, pennsylvania_railroad, bo_railroad, reading_railroad, short_line_railroad):
    """
    Test play_turn_property when player already owns all the railroads
    """
    arvind.cash = 2000
    buy_color_set(arvind, [pennsylvania_railroad, bo_railroad, reading_railroad, short_line_railroad])

    assert play_turn_railroad(pennsylvania_railroad, arvind) == []
