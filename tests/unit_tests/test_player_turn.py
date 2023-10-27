import pytest

from player_turn import run_player_option


@pytest.mark.parametrize("asset",["st_charles_place", "pennsylvania_railroad", "electric_company"])
@pytest.mark.parametrize("option", [0, 1])
def test_run_player_option_buy_asset(mocker, arvind, st_charles_place, pennsylvania_railroad, electric_company, option, request, asset):
    """
    Test run_player_option
    """
    def mock_buy_asset(player, test_asset):
        test_asset.owner = player
    option_function_dict = {0: 'Buy asset', 1: 'Do nothing'}
    asset = request.getfixturevalue(asset)
    mocker.patch.object(arvind, 'buy_asset', side_effect=mock_buy_asset(arvind, asset))
    run_player_option(arvind, asset, option_function_dict, option)

    assert asset.owner == arvind
    assert asset in arvind.player_portfolio
