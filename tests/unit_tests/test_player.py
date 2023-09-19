import pytest

from Player import Player


def test_init_default_values():
    arvind = Player("Arvind")

    assert arvind.cash == 200
    assert arvind.networth == 0
    assert arvind.tile_no == 0

def test_init_correct_values():
    arvind = Player("Arvind", 500)

    assert arvind.name == "Arvind"
    assert arvind.cash == 500


def test_buy_property(states_avenue_fx, arvind_fx, st_charles_place_fx):
    arvind_fx.cash = 500
    arvind_fx.buy_property(states_avenue_fx)

    assert arvind_fx.cash == 360
    assert states_avenue_fx in arvind_fx.player_portfolio

    arvind_fx.cash = 10
    arvind_fx.buy_property(st_charles_place_fx)

    assert arvind_fx.cash == 10
    assert st_charles_place_fx not in arvind_fx.player_portfolio

@pytest.mark.parametrize("current_tile, expected_current_tile, expected_cash",[
    (0, 12, 200),
    (28, 0, 200),
    (39, 11, 400)
])
def test_move(arvind_fx, pennsylvania_railroad_fx, st_james_place_fx, current_tile, expected_current_tile, expected_cash):
    arvind_fx.tile_no = current_tile
    arvind_fx.move(12)
    assert arvind_fx.tile_no == expected_current_tile
    assert arvind_fx.cash == expected_cash
    assert arvind_fx.tile_no < 39

# def test_move_to(arvind_fx, states_avenue_fx):
#     arvind_fx.move_to(states_avenue_fx)
#     assert arvind_fx.tile_no == 13

def test_pay_rent(arvind_fx, arun_fx):
    arvind_fx.pay_rent(arun_fx, 20)
    assert arvind_fx.cash == 180
    assert arun_fx.cash == 220

# test git hook 3