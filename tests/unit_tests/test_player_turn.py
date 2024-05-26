from player_turn import get_properties_for_mortgaging, get_properties_for_unmortgaging
from tests.common import buy_assets


# import pytest
#
# from player_turn import run_player_option
#
#
# @pytest.mark.parametrize("asset",["st_charles_place", "pennsylvania_railroad", "electric_company"])
# @pytest.mark.parametrize("option", [0])
# def test_run_player_option_buy_asset(mocker, arvind, st_charles_place, pennsylvania_railroad, electric_company, option, request, asset):
#     """
#     Test run_player_option for buy_property
#     """
#     def mock_buy_asset(player, test_asset):
#         test_asset.owner = player
#     option_function_dict = {0: 'Buy property', 1: 'End turn'}
#     asset = request.getfixturevalue(asset)
#     mocker.patch.object(arvind, 'buy_asset', side_effect=mock_buy_asset(arvind, asset))
#     mocker.patch('player_turn.get_properties_for_building_houses', return_value=[])
#     run_player_option(arvind, asset, option_function_dict[option])
#
#     assert asset.owner == arvind
#     assert asset in arvind.player_portfolio
#
# @pytest.mark.parametrize("asset",["st_charles_place"])
# @pytest.mark.parametrize("option", [0])
# def test_run_player_option_build_house(mocker, arvind, st_charles_place, option, request, asset):
#     """
#     Test run_player_option for build_house
#     """
#     def mock_build_house(test_asset):
#         test_asset._houses += 1
#     mocker.patch('player_turn.')
#     option_function_dict = {0: 'Build house', 1: 'End turn'}
#     asset = request.getfixturevalue(asset)
#     asset.owner = arvind
#     mocker.patch.object(arvind, 'build_house', side_effect=mock_build_house(asset))
#     run_player_option(arvind, asset, option_function_dict[option])
#
# @pytest.mark.parametrize("asset",["st_charles_place"])
# @pytest.mark.parametrize("option", [0])
# def test_run_player_option_build_hotel(mocker, arvind, st_charles_place, option, request, asset):
#     """
#     Test run_player_option for build_hotel
#     """
#     def mock_build_hotel(test_asset):
#         test_asset._hotel = True
#
#     option_function_dict = {0: 'Build hotel', 1: 'End turn'}
#     asset = request.getfixturevalue(asset)
#     asset.owner = arvind
#     mocker.patch.object(arvind, 'build_hotel', side_effect=mock_build_hotel(asset))
#     run_player_option(arvind, asset, option_function_dict[option])
#
# @pytest.mark.parametrize("asset",["st_charles_place"])
# @pytest.mark.parametrize("option", [0, 1])
# def test_run_player_option_sell_house(mocker, arvind, st_charles_place, option, request, asset):
#     """
#     Test run_player_option for sell_house
#     """
#     def mock_sell_house(test_asset):
#         test_asset._houses -= 1
#
#     option_function_dict = {0: 'Sell house', 1: 'End turn'}
#     asset = request.getfixturevalue(asset)
#     asset.owner = arvind
#     mocker.patch.object(arvind, 'sell_house', side_effect=mock_sell_house(asset))
#     run_player_option(arvind, asset, option_function_dict[option])
#
# @pytest.mark.parametrize("asset",["st_charles_place"])
# @pytest.mark.parametrize("option", [0, 1])
# def test_run_player_option_sell_hotel(mocker, arvind, st_charles_place, option, request, asset):
#     """
#     Test run_player_option for sell_hotel
#     """
#     def mock_sell_hotel(test_asset):
#         test_asset._hotel = False
#
#     option_function_dict = {0: 'Sell house', 1: 'End turn'}
#     asset = request.getfixturevalue(asset)
#     asset.owner = arvind
#     asset._hotel = True
#     mocker.patch.object(arvind, 'sell_house', side_effect=mock_sell_hotel(asset))
#     run_player_option(arvind, asset, option_function_dict[option])

def test_get_properties_for_mortgaging_1(arvind, states_avenue, st_charles_place, st_james_place, bo_railroad, water_works):
    """
    Test get_properties_for_mortgaging when some of the properties are mortgaged
    :param arvind: The player trying to get the list of properties that can be mortgaged
    """
    arvind.cash = 1500
    buy_assets(arvind, [states_avenue, st_charles_place, st_james_place, bo_railroad, water_works])
    arvind.mortgage_property(states_avenue)
    arvind.mortgage_property(bo_railroad)
    arvind.mortgage_property(water_works)
    unmortgaged_properties_list = get_properties_for_mortgaging(arvind)
    for each in unmortgaged_properties_list:
        assert each in [st_charles_place, st_james_place]

def test_get_properties_for_mortgaging_2(arvind, states_avenue, st_charles_place, st_james_place):
    """
    Test get_properties_for_mortgaging when none of the properties are mortgaged
    :param arvind: The player trying to get the list of properties that can be mortgaged
    """
    arvind.cash = 1500
    buy_assets(arvind, [states_avenue, st_charles_place, st_james_place])
    expected = [states_avenue, st_charles_place, st_james_place]
    unmortgaged_properties_list = get_properties_for_mortgaging(arvind)
    for each in unmortgaged_properties_list:
        assert each in expected

def test_get_properties_for_unmortgaging(arvind, states_avenue, st_charles_place, st_james_place, bo_railroad, water_works):
    """
    Test get_properties_for_unmortgaging when some of the properties are unmortgaged
    :param arvind: The player trying to get the list of properties that can be unmortgaged
    """
    arvind.cash = 1500
    buy_assets(arvind, [states_avenue, st_charles_place, st_james_place, bo_railroad, water_works])
    arvind.mortgage_property(states_avenue)
    arvind.mortgage_property(bo_railroad)
    arvind.mortgage_property(water_works)
    mortgaged_properties_list = get_properties_for_unmortgaging(arvind)
    for each in mortgaged_properties_list:
        assert each in [states_avenue, bo_railroad, water_works]