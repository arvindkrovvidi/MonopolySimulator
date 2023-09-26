import pytest

from ChanceTile import get_nearest_railroad, execute_chance_5
from Property_data import raiload_properties_list
from TileIterators import TileDict


@pytest.mark.parametrize("input_tile_no, expected", [
    (7, 5),
    (22, 25),
    (36, 35)
])
def test_get_nearest_railroad(arvind_fx, input_tile_no, expected):
    arvind_fx.tile_no = input_tile_no
    assert get_nearest_railroad(arvind_fx) == raiload_properties_list[expected]


def test_execute_chance_5_railroad_free(arvind_fx, mocker, pennsylvania_railroad_fx):
    arvind_fx.tile_no = 36
    property_tracker = TileDict({})
    mocker.patch("ChanceTile.get_nearest_railroad", return_value=pennsylvania_railroad_fx)
    execute_chance_5(arvind_fx, property_tracker)
    assert pennsylvania_railroad_fx in arvind_fx.player_portfolio

def test_execute_chance_5_railroad_occupied(arvind_fx, arun_fx, mocker, pennsylvania_railroad_fx):
    arvind_fx.tile_no = 36
    property_tracker = TileDict({pennsylvania_railroad_fx: arun_fx})
    mocker.patch("ChanceTile.get_nearest_railroad", return_value=pennsylvania_railroad_fx)
    execute_chance_5(arvind_fx, property_tracker)
    assert arun_fx.cash == 200 + (pennsylvania_railroad_fx.rent * 2)
    assert arvind_fx.cash == 200 - (pennsylvania_railroad_fx.rent * 2)