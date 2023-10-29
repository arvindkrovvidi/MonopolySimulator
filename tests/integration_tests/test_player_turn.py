import pytest

from player_turn import run_player_option, get_available_options_properties


def buy_color_set(player, asset_1, asset_2, asset_3):
    for asset in [asset_1, asset_2, asset_3]:
        player.buy_asset(asset)
def build_houses(player, asset_1, asset_2, asset_3, num_houses):
    buy_color_set(player, asset_1, asset_2, asset_3)
    for i in range(0,num_houses):
        for asset in [asset_1, asset_2, asset_3]:
            player.build_house(asset)

def build_all_hotels(player, asset_1, asset_2, asset_3):
    build_houses(player, asset_1, asset_2, asset_3, 4)
    for asset in [asset_1, asset_2, asset_3]:
        player.build_hotel(asset)

@pytest.mark.parametrize("asset",["st_charles_place", "pennsylvania_railroad", "electric_company"])
@pytest.mark.parametrize("option", [0])
def test_run_player_option_buy_asset(arvind, st_charles_place, pennsylvania_railroad, electric_company, option, request, asset):
    """
    Test run_player_option for buy_property
    """
    option_function_dict = {0: 'Buy property', 1: 'Do nothing'}
    asset = request.getfixturevalue(asset)
    run_player_option(arvind, asset, option_function_dict, option)

    assert asset.owner == arvind
    assert asset in arvind.player_portfolio

def test_run_player_option_build_house(arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for build_house
    """
    arvind.cash = 1000
    option_function_dict = {0: 'Build house', 1: 'Do nothing'}
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
    option_function_dict = {0: 'Build hotel', 1: 'Do nothing'}
    build_houses(arvind, st_charles_place, virginia_avenue, states_avenue, 4)
    run_player_option(arvind, states_avenue, option_function_dict, 0)

    assert states_avenue._hotel == True

def test_run_player_option_sell_house(arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for sell_house
    """
    arvind.cash = 2000
    option_function_dict = {0: 'Sell house', 1: 'Do nothing'}
    buy_color_set(arvind, st_charles_place,states_avenue, virginia_avenue)
    arvind.build_house(states_avenue)
    assert states_avenue._houses == 1
    run_player_option(arvind, states_avenue, option_function_dict, 0)
    assert states_avenue._houses == 0

def test_run_player_option_sell_hotel(arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for sell_hotel
    """
    arvind.cash = 2000
    option_function_dict = {0: 'Sell hotel', 1: 'Do nothing'}
    build_houses(arvind, st_charles_place, states_avenue, virginia_avenue, 4)
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
    assert 'Do nothing' in available_options

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
    assert 'Do nothing' in available_options

def test_get_available_options_properties_3(arvind, states_avenue, st_charles_place, virginia_avenue):
    """
    Test the available_options list when player lands on an asset owned by them, and they have the color set
    """
    arvind.cash = 1500
    arvind.move_to(states_avenue.tile_no, collect_go_cash_flag=False)
    current_tile = states_avenue
    buy_color_set(arvind, st_charles_place, states_avenue, virginia_avenue)

    available_options = get_available_options_properties(current_tile, arvind)
    assert 'Buy property' not in available_options
    assert 'Build house' in available_options
    assert 'Build hotel' not in available_options
    assert 'Sell house' not in available_options
    assert 'Sell hotel' not in available_options
    assert 'Do nothing' in available_options

def test_get_available_options_properties_4(arvind, states_avenue, st_charles_place, virginia_avenue):
    """
    Test the available_options list when player lands on an asset owned by them, and they have 4 houses in all the properties in the color set.
    """
    arvind.cash = 2000
    arvind.move_to(states_avenue.tile_no, collect_go_cash_flag=False)
    current_tile = states_avenue
    build_houses(arvind, st_charles_place, states_avenue, virginia_avenue, 4)
    available_options = get_available_options_properties(current_tile, arvind)
    assert 'Buy property' not in available_options
    assert 'Build house' not in available_options
    assert 'Build hotel' in available_options
    assert 'Sell house' in available_options
    assert 'Sell hotel' not in available_options
    assert 'Do nothing' in available_options

def test_get_available_options_properties_5(arvind, states_avenue, st_charles_place, virginia_avenue):
    """
    Test the available_options list when player lands on an asset owned by them, and they have hotels in all the properties in the color set.
    """
    arvind.cash = 2000
    arvind.move_to(states_avenue.tile_no, collect_go_cash_flag=False)
    current_tile = states_avenue
    build_all_hotels(arvind, st_charles_place, states_avenue, virginia_avenue)
    available_options = get_available_options_properties(current_tile, arvind)
    assert 'Buy property' not in available_options
    assert 'Build house' not in available_options
    assert 'Build hotel' not in available_options
    assert 'Sell house' not in available_options
    assert 'Sell hotel' in available_options
    assert 'Do nothing' in available_options
