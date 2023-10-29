import pytest

from player_turn import run_player_option


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
    arvind.buy_asset(st_charles_place)
    arvind.buy_asset(virginia_avenue)
    arvind.buy_asset(states_avenue)
    arvind.build_house(st_charles_place)
    arvind.build_house(virginia_avenue)
    arvind.build_house(states_avenue)
    arvind.build_house(st_charles_place)
    arvind.build_house(virginia_avenue)
    arvind.build_house(states_avenue)
    arvind.build_house(st_charles_place)
    arvind.build_house(virginia_avenue)
    arvind.build_house(states_avenue)
    arvind.build_house(st_charles_place)
    arvind.build_house(virginia_avenue)
    arvind.build_house(states_avenue)
    run_player_option(arvind, states_avenue, option_function_dict, 0)

    assert states_avenue._hotel == True

def test_run_player_option_sell_house(arvind, st_charles_place, virginia_avenue, states_avenue):
    """
    Test run_player_option for sell_house
    """
    arvind.cash = 2000
    option_function_dict = {0: 'Sell house', 1: 'Do nothing'}
    arvind.buy_asset(st_charles_place)
    arvind.buy_asset(virginia_avenue)
    arvind.buy_asset(states_avenue)
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
    arvind.buy_asset(st_charles_place)
    arvind.buy_asset(virginia_avenue)
    arvind.buy_asset(states_avenue)
    arvind.build_house(st_charles_place)
    arvind.build_house(virginia_avenue)
    arvind.build_house(states_avenue)
    arvind.build_house(st_charles_place)
    arvind.build_house(virginia_avenue)
    arvind.build_house(states_avenue)
    arvind.build_house(st_charles_place)
    arvind.build_house(virginia_avenue)
    arvind.build_house(states_avenue)
    arvind.build_house(st_charles_place)
    arvind.build_house(virginia_avenue)
    arvind.build_house(states_avenue)
    arvind.build_hotel(states_avenue)
    assert states_avenue._hotel == True
    run_player_option(arvind, states_avenue, option_function_dict, 0)

    assert states_avenue._hotel == False