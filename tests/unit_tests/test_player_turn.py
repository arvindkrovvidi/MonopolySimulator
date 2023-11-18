import pytest

from player_turn import run_player_option


@pytest.mark.parametrize("asset",["st_charles_place", "pennsylvania_railroad", "electric_company"])
@pytest.mark.parametrize("option", [0])
def test_run_player_option_buy_asset(mocker, arvind, st_charles_place, pennsylvania_railroad, electric_company, option, request, asset):
    """
    Test run_player_option for buy_property
    """
    def mock_buy_asset(player, test_asset):
        test_asset.owner = player
    option_function_dict = {0: 'Buy property', 1: 'End turn'}
    asset = request.getfixturevalue(asset)
    mocker.patch.object(arvind, 'buy_asset', side_effect=mock_buy_asset(arvind, asset))
    run_player_option(arvind, asset, option_function_dict[option])

    assert asset.owner == arvind
    assert asset in arvind.player_portfolio

@pytest.mark.parametrize("asset",["st_charles_place"])
@pytest.mark.parametrize("option", [0])
def test_run_player_option_build_house(mocker, arvind, st_charles_place, option, request, asset):
    """
    Test run_player_option for build_house
    """
    def mock_build_house(test_asset):
        test_asset._houses += 1

    option_function_dict = {0: 'Build house', 1: 'End turn'}
    asset = request.getfixturevalue(asset)
    asset.owner = arvind
    mocker.patch.object(arvind, 'build_house', side_effect=mock_build_house(asset))
    run_player_option(arvind, asset, option_function_dict[option])

@pytest.mark.parametrize("asset",["st_charles_place"])
@pytest.mark.parametrize("option", [0])
def test_run_player_option_build_hotel(mocker, arvind, st_charles_place, option, request, asset):
    """
    Test run_player_option for build_hotel
    """
    def mock_build_hotel(test_asset):
        test_asset._hotel = True

    option_function_dict = {0: 'Build hotel', 1: 'End turn'}
    asset = request.getfixturevalue(asset)
    asset.owner = arvind
    mocker.patch.object(arvind, 'build_hotel', side_effect=mock_build_hotel(asset))
    run_player_option(arvind, asset, option_function_dict[option])

@pytest.mark.parametrize("asset",["st_charles_place"])
@pytest.mark.parametrize("option", [0, 1])
def test_run_player_option_sell_house(mocker, arvind, st_charles_place, option, request, asset):
    """
    Test run_player_option for sell_house
    """
    def mock_sell_house(test_asset):
        test_asset._houses -= 1

    option_function_dict = {0: 'Sell house', 1: 'End turn'}
    asset = request.getfixturevalue(asset)
    asset.owner = arvind
    mocker.patch.object(arvind, 'sell_house', side_effect=mock_sell_house(asset))
    run_player_option(arvind, asset, option_function_dict[option])

@pytest.mark.parametrize("asset",["st_charles_place"])
@pytest.mark.parametrize("option", [0, 1])
def test_run_player_option_sell_hotel(mocker, arvind, st_charles_place, option, request, asset):
    """
    Test run_player_option for sell_hotel
    """
    def mock_sell_hotel(test_asset):
        test_asset._hotel = False

    option_function_dict = {0: 'Sell house', 1: 'End turn'}
    asset = request.getfixturevalue(asset)
    asset.owner = arvind
    asset._hotel = True
    mocker.patch.object(arvind, 'sell_house', side_effect=mock_sell_hotel(asset))
    run_player_option(arvind, asset, option_function_dict[option])