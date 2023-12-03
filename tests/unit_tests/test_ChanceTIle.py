import pytest

from Tiles.ChanceTile import get_nearest_railroad, execute_chance_5, execute_chance_7, get_nearest_utility, \
    execute_chance_15, execute_chance_12
from Tiles_data.railroad_property_data import railroad_properties_list
from Tiles_data.utilities_data import utilities_list


@pytest.mark.parametrize("input_tile_no, expected", [
    (7, 5),
    (22, 25),
    (36, 35)
])
def test_get_nearest_railroad(arvind, input_tile_no, expected):
    arvind.tile_no = input_tile_no
    assert get_nearest_railroad(arvind) == railroad_properties_list[expected]


def test_execute_chance_5_railroad_free(arvind, mocker, pennsylvania_railroad):
    arvind.tile_no = 36
    mocker.patch("Tiles.ChanceTile.get_nearest_railroad", return_value=pennsylvania_railroad)
    execute_chance_5(arvind)
    assert arvind.current_tile == pennsylvania_railroad

@pytest.mark.parametrize("input_tile_no, expected", [
    (7, 12),
    (22, 28),
    (36, 28)
])
def test_get_nearest_utility(arvind, input_tile_no, expected):
    arvind.tile_no = input_tile_no
    assert get_nearest_utility(arvind) == utilities_list[expected]


def test_execute_chance_7_utility_free(arvind, mocker, electric_company):
    arvind.tile_no = 36
    mocker.patch("Tiles.ChanceTile.get_nearest_utility", return_value=electric_company)
    execute_chance_7(arvind, 5)
    assert arvind.current_tile == electric_company

def test_execute_chance_15(arvind, arun, adityam, padma):
    arvind.cash = 500
    all_players_list = [arvind, arun, adityam, padma]
    execute_chance_15(arvind, all_players_list)
    assert arvind.cash == 350
    assert arun.cash == 250
    assert adityam.cash == 250
    assert padma.cash == 250


def test_execute_chance_12(arvind, states_avenue, virginia_avenue, st_james_place):
    arvind.cash = 500
    arvind.player_portfolio.append(states_avenue)
    arvind.player_portfolio.append(virginia_avenue)
    arvind.player_portfolio.append(st_james_place)
    states_avenue._houses = 2
    virginia_avenue._houses = 2
    st_james_place._hotel = True

    execute_chance_12(arvind)
    assert arvind.cash == 300
