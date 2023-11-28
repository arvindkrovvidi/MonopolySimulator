import pytest

from player_turn import run_player_option, get_available_options_assets, play_turn_jail, play_turn_asset, play_turn, \
    get_properties_for_building_houses, get_properties_for_selling_houses, get_properties_for_building_hotels, \
    get_properties_for_selling_hotels
from tests.common import build_houses, build_all_hotels, buy_assets


@pytest.mark.parametrize("asset", ["st_charles_place", "pennsylvania_railroad", "electric_company"])
@pytest.mark.parametrize("option", [0])
def test_run_player_option_buy_asset(arvind, st_charles_place, pennsylvania_railroad, electric_company, option, request,
                                     asset):
    """
    Test run_player_option for buy_property
    """
    asset = request.getfixturevalue(asset)
    run_player_option(arvind, asset, 'Buy property')

    assert asset.owner == arvind
    assert asset in arvind.player_portfolio


def test_run_player_option_build_house(mocker, arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for build_house
    """
    arvind.cash = 1000
    mocker.patch('player_turn.input', return_value='0')
    arvind.buy_asset(st_charles_place)
    arvind.buy_asset(virginia_avenue)
    arvind.buy_asset(states_avenue)
    run_player_option(arvind, st_charles_place, 'Build house')

    assert st_charles_place._houses == 1


def test_run_player_option_build_hotel(mocker, arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for build_hotel
    """
    arvind.cash = 2000
    mocker.patch('player_turn.input', return_value='2')
    build_houses(arvind, [st_charles_place, virginia_avenue, states_avenue], 4)
    run_player_option(arvind, states_avenue, 'Build hotel')

    assert states_avenue._hotel == True


def test_run_player_option_sell_house(mocker, arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for sell_house
    """
    arvind.cash = 2000
    mocker.patch('player_turn.input', return_value='0')
    buy_assets(arvind, [st_charles_place, states_avenue, virginia_avenue])
    arvind.build_house(states_avenue)
    assert states_avenue._houses == 1
    run_player_option(arvind, states_avenue, 'Sell house')
    assert states_avenue._houses == 0


def test_run_player_option_sell_hotel(mocker, arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for sell_hotel
    """
    arvind.cash = 2000
    mocker.patch('player_turn.input', return_value='0')
    build_houses(arvind, [st_charles_place, states_avenue, virginia_avenue], 4)
    arvind.build_hotel(states_avenue)
    assert states_avenue._hotel == True
    run_player_option(arvind, states_avenue, 'Sell hotel')
    assert states_avenue._hotel == False


def test_get_available_options_properties_1(arvind, states_avenue):
    """
    Test the available_options list when player lands on a free asset
    """
    arvind.move_to(states_avenue.tile_no, collect_go_cash_flag=False)
    current_tile = states_avenue
    available_options = get_available_options_assets(current_tile, arvind)
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
    available_options = get_available_options_assets(current_tile, arvind)
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
    buy_assets(arvind, [st_charles_place, states_avenue, virginia_avenue])

    available_options = get_available_options_assets(current_tile, arvind)
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
    available_options = get_available_options_assets(current_tile, arvind)
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
    available_options = get_available_options_assets(current_tile, arvind)
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
    mocker.patch('player_turn.input', side_effect=['1', '0', '0'])
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
    mocker.patch('player_turn.input', side_effect=['1', '1', '1', '0', '0'])
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[2, 3, 2, 3, 2, 3])

    play_turn_jail(arvind)
    play_turn_jail(arvind)
    play_turn_jail(arvind)

    assert arvind.cash == 250
    assert arvind.in_jail == False
    assert arvind.tile_no == 15
    assert pennsylvania_railroad in arvind.player_portfolio


@pytest.mark.skip(reason="properties inside all_tiles_list not getting reset after previous test.")
def test_play_turn_jail_5(mocker, arvind, pennsylvania_railroad, all_tiles_list):
    """
    Test play_turn_jail when the player fails to throw double in first try and pays fine in second try.
    """
    arvind.cash = 500
    all_tiles_list.append(pennsylvania_railroad)
    arvind.move_to(10, collect_go_cash_flag=False)
    mocker.patch('player_turn.input', side_effect=['1', '0', '0'])
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[2, 3, 2, 3])
    mocker.patch('player_turn.current_tile', return_value=pennsylvania_railroad)
    play_turn_jail(arvind)
    play_turn_jail(arvind)

    assert arvind.cash == 250
    assert arvind.in_jail == False
    assert arvind.tile_no == 15
    assert pennsylvania_railroad in arvind.player_portfolio


@pytest.mark.skip(reason="properties inside all_tiles_list not getting reset after previous test.")
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
    Test play_turn_asset when the property is free.
    """

    assert play_turn_asset(states_avenue, arvind) == ['Buy property']
    assert arvind.cash == 200


def test_play_turn_property_2(arvind, states_avenue):
    """
    Test play_turn_asset when the player already owns the property.
    """

    arvind.buy_asset(states_avenue)
    assert play_turn_asset(states_avenue, arvind) == []
    assert arvind.cash == 60


def test_play_turn_property_3(arvind, states_avenue, arun):
    """
    Test play_turn_asset when another player owns the property.
    """

    arun.buy_asset(states_avenue)
    assert play_turn_asset(states_avenue, arvind) == []
    assert arvind.cash == 190
    assert arun.cash == 70
    assert states_avenue in arun.player_portfolio


def test_play_turn_property_4(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_asset when the player owns the color set.
    """
    arvind.cash = 2000

    buy_assets(arvind, [states_avenue, virginia_avenue, st_charles_place])
    assert play_turn_asset(states_avenue, arvind) == ['Build house']


def test_play_turn_property_5(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_asset when the player has less than 4 houses on any property.
    """
    arvind.cash = 2000

    build_houses(arvind, [states_avenue, virginia_avenue, st_charles_place], 3)
    assert play_turn_asset(states_avenue, arvind) == ['Build house', 'Sell house']


def test_play_turn_property_6(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_asset when the player has 4 houses on all properties.
    """
    arvind.cash = 2000

    build_houses(arvind, [states_avenue, virginia_avenue, st_charles_place], 4)
    assert play_turn_asset(states_avenue, arvind) == ['Build hotel', 'Sell house']


def test_play_turn_property_7(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_asset when the player has a hotel on the property.
    """
    arvind.cash = 2000

    build_houses(arvind, [states_avenue, virginia_avenue, st_charles_place], 4)
    arvind.build_hotel(states_avenue)
    assert play_turn_asset(states_avenue, arvind) == ['Sell hotel']


def test_play_turn_property_8(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_asset when the player has a hotel on a different property in the same color set.
    """
    arvind.cash = 2000

    build_houses(arvind, [states_avenue, virginia_avenue, st_charles_place], 4)
    arvind.build_hotel(virginia_avenue)
    assert play_turn_asset(states_avenue, arvind) == ['Build hotel', 'Sell house']


def test_play_turn_property_9(arvind, states_avenue, virginia_avenue, st_charles_place):
    """
    Test play_turn_asset when the player has a hotel on all the properties in the color set.
    """
    arvind.cash = 2000

    build_all_hotels(arvind, [states_avenue, virginia_avenue, st_charles_place])
    assert play_turn_asset(states_avenue, arvind) == ['Sell hotel']


# def test_play_turn_railroad_1(arvind, pennsylvania_railroad):
#     """
#     Test play_turn_asset when the railroad is free.
#     """
#
#     assert play_turn_railroad(pennsylvania_railroad, arvind) == ['Buy property']
#     assert arvind.cash == 200


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

def test_play_turn_utility_1(arvind, electric_company):
    """
    Test play_turn_property when the utility is free.
    """
    throw = arvind.throw_dice()
    assert play_turn_utility(electric_company, arvind, throw) == ['Buy property']
    assert arvind.cash == 200

def test_play_turn_utility_2(arvind, electric_company):
    """
    Test play_turn_property when the player already owns the utility.
    """
    throw = arvind.throw_dice()
    arvind.buy_asset(electric_company)
    assert play_turn_utility(electric_company, arvind, throw) == []
    assert arvind.cash == 50

def test_play_turn_utility_3(mocker, arvind, arun, electric_company):
    """
    Test play_turn_property when another player already owns the railroad.
    """
    mocker.patch.object(arun, 'throw_dice', return_value=5)
    throw = arun.throw_dice()
    arun.buy_asset(electric_company)

    assert play_turn_utility(electric_company, arvind, throw) == []
    assert arvind.cash == 180
    assert arun.cash == 70

def test_play_turn_utility_4(arvind, pennsylvania_railroad, bo_railroad, reading_railroad, short_line_railroad):
    """
    Test play_turn_property when player already owns all the railroads
    """
    arvind.cash = 2000
    buy_color_set(arvind, [pennsylvania_railroad, bo_railroad, reading_railroad, short_line_railroad])

    assert play_turn_railroad(pennsylvania_railroad, arvind) == []

def test_play_turn_1(mocker, arvind, chance_22):
    """
    Test play_turn when player lands on chance 22 and picks chance card 10
    """
    arvind.move_to(22, collect_go_cash_flag=False)
    mocker.patch('player_turn.randint', return_value=10)
    current_tile = chance_22
    mocker.patch('player_turn.input', return_value=0)
    play_turn(arvind, current_tile)

    assert arvind.tile_no == 19
    assert arvind.cash == 0

def test_play_turn_2(mocker, arvind, chance_7):
    """
    Test play_turn when player lands on chance 7 and picks chance card 10
    """
    arvind.move_to(7, collect_go_cash_flag=False)
    current_tile = chance_7
    mocker.patch('player_turn.randint', return_value=10)

    play_turn(arvind, current_tile)

    assert arvind.tile_no == 4
    assert arvind.cash == 0

def test_play_turn_3(mocker, arvind, chance_36):
    """
    Test play_turn when player lands on chance 36 and picks chance card 10
    """
    arvind.move_to(36, collect_go_cash_flag=False)
    current_tile = chance_36
    mocker.patch('player_turn.randint', side_effect=[10, 8])

    play_turn(arvind, current_tile)

    assert arvind.tile_no == 33
    assert arvind.cash == 220

def test_play_turn_4(mocker, arvind, states_avenue, st_charles_place, virginia_avenue, all_tiles_list):
    """
    Test play_turn when player builds 2 houses in the same turn
    """
    arvind.cash = 2000
    mocker.patch('player_turn.input', side_effect=['0', '0', '1'])
    mocker.patch('player_turn.all_tiles_list', return_value=all_tiles_list)
    build_houses(arvind, [st_charles_place, states_avenue, virginia_avenue], 1)
    arvind.build_house(st_charles_place)
    arvind.build_house(virginia_avenue)
    arvind.move_to(states_avenue.tile_no)
    current_tile = states_avenue

    assert st_charles_place._houses == 2
    assert virginia_avenue._houses == 2

    play_turn(arvind, current_tile)

    assert states_avenue._houses == 3


def test_get_properties_for_building_houses_1(states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad, electric_company, arvind, st_james_place):
    """
    Test get_properties_for_building_houses when the player has one color set and the properties in the color set do not have any houses
    """
    arvind.cash = 1500
    buy_assets(arvind, [states_avenue, st_charles_place, virginia_avenue])
    arvind.buy_asset(pennsylvania_railroad)
    arvind.buy_asset(electric_company)
    arvind.buy_asset(st_james_place)

    properties_list = get_properties_for_building_houses(arvind)
    assert states_avenue in properties_list
    assert st_charles_place in properties_list
    assert virginia_avenue in properties_list
    assert pennsylvania_railroad not in properties_list
    assert electric_company not in properties_list
    assert st_james_place not in properties_list

def test_get_properties_for_building_houses_2(states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad, electric_company, arvind, st_james_place):
    """
    Test get_properties_for_building_houses when the player has one color set and the properties in the color set have equal number of houses
    """
    arvind.cash = 1500
    build_houses(arvind, [states_avenue, st_charles_place, virginia_avenue], 1)

    properties_list = get_properties_for_building_houses(arvind)
    assert states_avenue in properties_list
    assert st_charles_place in properties_list
    assert virginia_avenue in properties_list
    assert pennsylvania_railroad not in properties_list
    assert electric_company not in properties_list
    assert st_james_place not in properties_list

def test_get_properties_for_building_houses_3(states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad, electric_company, arvind, st_james_place):
    """
    Test get_properties_for_building_houses when the player has one color set and the properties in the color set have equal number of houses
    """
    arvind.cash = 1500
    build_houses(arvind, [states_avenue, st_charles_place, virginia_avenue], 1)
    arvind.build_house(states_avenue)
    properties_list = get_properties_for_building_houses(arvind)

    assert states_avenue not in properties_list
    assert st_charles_place in properties_list
    assert virginia_avenue in properties_list
    assert pennsylvania_railroad not in properties_list
    assert electric_company not in properties_list
    assert st_james_place not in properties_list

def test_get_properties_for_building_houses_4(states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad,
                                              electric_company, arvind, st_james_place, tennessee_avenue, new_york_avenue):
    """
    Test get_properties_for_building_houses when the player has one color set and the properties in the color set have equal number of houses
    """
    arvind.cash = 5000
    build_houses(arvind, [states_avenue, st_charles_place, virginia_avenue], 1)
    build_houses(arvind, [tennessee_avenue, st_james_place, new_york_avenue], 1)
    properties_list = get_properties_for_building_houses(arvind)

    assert states_avenue in properties_list
    assert st_charles_place in properties_list
    assert virginia_avenue in properties_list
    assert pennsylvania_railroad not in properties_list
    assert electric_company not in properties_list
    assert st_james_place in properties_list
    assert tennessee_avenue in properties_list
    assert new_york_avenue in properties_list

def test_get_properties_for_selling_houses_1(arvind, states_avenue, st_charles_place, virginia_avenue, st_james_place, pennsylvania_railroad, electric_company):
    """
    Test get_properties_for_selling_houses when player has hotels on all properties in the color set
    """
    arvind.cash = 3000
    build_all_hotels(arvind, [states_avenue, st_charles_place, virginia_avenue])
    buy_assets(arvind, [pennsylvania_railroad, electric_company, st_james_place])

    properties_list = get_properties_for_selling_houses(arvind)

    assert properties_list == []

def test_get_properties_for_selling_houses_2(arvind, states_avenue, st_charles_place, virginia_avenue, st_james_place, pennsylvania_railroad, electric_company):
    """
    Test get_properties_for_selling_houses when player has 4 houses on all properties in the color set
    """
    arvind.cash = 3000
    build_houses(arvind, [states_avenue, st_charles_place, virginia_avenue], 4)
    buy_assets(arvind, [pennsylvania_railroad, electric_company, st_james_place])
    properties_list = get_properties_for_selling_houses(arvind)

    assert states_avenue in properties_list
    assert st_charles_place in properties_list
    assert virginia_avenue in properties_list
    assert pennsylvania_railroad not in properties_list
    assert electric_company not in properties_list
    assert st_james_place not in properties_list

def test_get_properties_for_selling_houses_3(arvind, states_avenue, st_charles_place, virginia_avenue, st_james_place, pennsylvania_railroad, electric_company):
    """
    Test get_properties_for_selling_houses when player has 4 houses on all properties in the color set
    """
    arvind.cash = 3000
    build_houses(arvind, [states_avenue, st_charles_place, virginia_avenue], 3)
    buy_assets(arvind, [pennsylvania_railroad, electric_company, st_james_place])
    arvind.build_house(states_avenue)
    arvind.build_house(st_charles_place)
    properties_list = get_properties_for_selling_houses(arvind)

    assert states_avenue in properties_list
    assert st_charles_place in properties_list
    assert virginia_avenue not in properties_list
    assert pennsylvania_railroad not in properties_list
    assert electric_company not in properties_list
    assert st_james_place not in properties_list


def test_get_properties_for_building_hotels_1(arvind, states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad, electric_company, st_james_place):
    """
    Test get_properties_for_building_hotels when player has 4 houses in all properties in the color set
    """
    arvind.cash = 3000
    build_houses(arvind, [states_avenue, st_charles_place, virginia_avenue], 4)
    buy_assets(arvind, [pennsylvania_railroad, electric_company, st_james_place])
    properties_list = get_properties_for_building_hotels(arvind)

    assert states_avenue in properties_list
    assert virginia_avenue in properties_list
    assert st_charles_place in properties_list
    assert pennsylvania_railroad not in properties_list
    assert electric_company not in properties_list
    assert st_james_place not in properties_list

def test_get_properties_for_building_hotels_2(arvind, states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad, electric_company, st_james_place):
    """
    Test get_properties_for_building_hotels when player has different number of houses in all properties in the color set
    """
    arvind.cash = 3000
    build_houses(arvind, [states_avenue, st_charles_place, virginia_avenue], 3)
    arvind.build_house(states_avenue)
    arvind.build_house(st_charles_place)
    buy_assets(arvind, [pennsylvania_railroad, electric_company, st_james_place])
    properties_list = get_properties_for_building_hotels(arvind)

    assert properties_list == []

def test_get_properties_for_building_hotels_3(arvind, states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad, electric_company, st_james_place):
    """
    Test get_properties_for_building_hotels when player has hotels in some properties in the color set
    """
    arvind.cash = 3000
    build_houses(arvind, [states_avenue, st_charles_place, virginia_avenue], 4)
    arvind.build_hotel(states_avenue)
    arvind.build_hotel(st_charles_place)
    buy_assets(arvind, [pennsylvania_railroad, electric_company, st_james_place])
    properties_list = get_properties_for_building_hotels(arvind)

    assert properties_list == [virginia_avenue]

def test_get_properties_for_building_hotels_4(arvind, states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad, electric_company, st_james_place, tennessee_avenue, new_york_avenue):
    """
    Test get_properties_for_building_hotels when player has hotels in some properties in the color set
    """
    arvind.cash = 4000
    build_houses(arvind, [states_avenue, st_charles_place, virginia_avenue], 4)
    build_houses(arvind, [new_york_avenue, tennessee_avenue, st_james_place], 4)
    buy_assets(arvind, [pennsylvania_railroad, electric_company])
    properties_list = get_properties_for_building_hotels(arvind)

    assert states_avenue in properties_list
    assert st_charles_place in properties_list
    assert virginia_avenue in properties_list
    assert pennsylvania_railroad not in properties_list
    assert electric_company not in properties_list
    assert st_james_place in properties_list
    assert tennessee_avenue in properties_list
    assert new_york_avenue in properties_list


def test_get_properties_for_selling_hotels_1(arvind, states_avenue, st_charles_place, virginia_avenue,
                                              pennsylvania_railroad, electric_company, st_james_place):
    """
    Test get_properties_for_selling_hotels when player has hotels in all properties in the color set
    """
    arvind.cash = 3000
    build_all_hotels(arvind, [states_avenue, st_charles_place, virginia_avenue])

    properties_list = get_properties_for_selling_hotels(arvind)

    assert states_avenue in properties_list
    assert virginia_avenue in properties_list
    assert st_charles_place in properties_list
    assert pennsylvania_railroad not in properties_list
    assert electric_company not in properties_list
    assert st_james_place not in properties_list

def test_get_properties_for_selling_hotels_2(arvind, states_avenue, st_charles_place, virginia_avenue,
                                              pennsylvania_railroad, electric_company, st_james_place):
    """
    Test get_properties_for_selling_hotels when player has hotels in some of the properties in the color set
    """
    arvind.cash = 3000
    build_houses(arvind, [states_avenue, st_charles_place, virginia_avenue], 4)
    arvind.build_hotel(states_avenue)
    arvind.build_hotel(st_charles_place)

    properties_list = get_properties_for_selling_hotels(arvind)

    assert states_avenue in properties_list
    assert virginia_avenue not in properties_list
    assert st_charles_place in properties_list
    assert pennsylvania_railroad not in properties_list
    assert electric_company not in properties_list
    assert st_james_place not in properties_list

def test_get_properties_for_selling_hotels_3(arvind, states_avenue, st_charles_place, virginia_avenue,
                                              pennsylvania_railroad, electric_company, st_james_place, tennessee_avenue, new_york_avenue):
    """
    Test get_properties_for_selling_hotels when player has hotels in all the properties for 2 color sets
    """
    arvind.cash = 5000
    build_all_hotels(arvind, [states_avenue, st_charles_place, virginia_avenue])
    build_all_hotels(arvind, [tennessee_avenue, new_york_avenue, st_james_place])

    properties_list = get_properties_for_selling_hotels(arvind)

    assert states_avenue in properties_list
    assert virginia_avenue in properties_list
    assert st_charles_place in properties_list
    assert pennsylvania_railroad not in properties_list
    assert electric_company not in properties_list
    assert st_james_place in properties_list
    assert new_york_avenue in properties_list
    assert tennessee_avenue in properties_list