import pytest

from ChanceTile import get_nearest_railroad, execute_chance_5, execute_chance_7, get_nearest_utility, execute_chance_15
from Property_data import railroad_properties_list, utilities_list


@pytest.mark.parametrize("input_tile_no, expected", [
    (7, 5),
    (22, 25),
    (36, 35)
])
def test_get_nearest_railroad(arvind_fx, input_tile_no, expected):
    arvind_fx.tile_no = input_tile_no
    assert get_nearest_railroad(arvind_fx) == railroad_properties_list[expected]


def test_execute_chance_5_railroad_free(arvind_fx, mocker, pennsylvania_railroad_fx):
    arvind_fx.tile_no = 36
    mocker.patch("ChanceTile.get_nearest_railroad", return_value=pennsylvania_railroad_fx)
    execute_chance_5(arvind_fx)
    assert pennsylvania_railroad_fx in arvind_fx.player_portfolio
    assert arvind_fx.tile_no == pennsylvania_railroad_fx.tile_no


def test_execute_chance_5_railroad_occupied(arvind_fx, arun_fx, mocker, pennsylvania_railroad_fx):
    arvind_fx.tile_no = 36
    pennsylvania_railroad_fx.owner = arun_fx
    mocker.patch("ChanceTile.get_nearest_railroad", return_value=pennsylvania_railroad_fx)
    execute_chance_5(arvind_fx)
    assert arun_fx.cash == 200 + (pennsylvania_railroad_fx.rent * 2)
    assert arvind_fx.cash == 200 - (pennsylvania_railroad_fx.rent * 2)
    assert arvind_fx.tile_no == pennsylvania_railroad_fx.tile_no


@pytest.mark.parametrize("input_tile_no, expected", [
    (7, 12),
    (22, 28),
    (36, 28)
])
def test_get_nearest_utility(arvind_fx, input_tile_no, expected):
    arvind_fx.tile_no = input_tile_no
    assert get_nearest_utility(arvind_fx) == utilities_list[expected]


def test_execute_chance_7_utility_free(arvind_fx, mocker, electric_company_fx):
    arvind_fx.tile_no = 36
    mocker.patch("ChanceTile.get_nearest_utility", return_value=electric_company_fx)
    execute_chance_7(arvind_fx)
    assert electric_company_fx in arvind_fx.player_portfolio
    assert arvind_fx.tile_no == electric_company_fx.tile_no


def test_execute_chance_7_utility_occupied(arvind_fx, arun_fx, mocker, electric_company_fx):
    arvind_fx.tile_no = 36
    electric_company_fx.owner = arun_fx
    mocker.patch("ChanceTile.get_nearest_utility", return_value=electric_company_fx)
    execute_chance_7(arvind_fx)
    assert arun_fx.cash == 200 + (electric_company_fx.rent * 2)
    assert arvind_fx.cash == 200 - (electric_company_fx.rent * 2)
    assert arvind_fx.tile_no == electric_company_fx.tile_no


def test_execute_chance_15(arvind_fx, arun_fx, adityam_fx, padma_fx):
    arvind_fx.cash = 500
    all_players_list = [arvind_fx, arun_fx, adityam_fx, padma_fx]
    execute_chance_15(arvind_fx, all_players_list)
    assert arvind_fx.cash == 350
    assert arun_fx.cash == 250
    assert adityam_fx.cash == 250
    assert padma_fx.cash == 250
