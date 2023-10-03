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


def test_buy_property(states_avenue, arvind_fx, st_charles_place):
    arvind_fx.cash = 500
    arvind_fx.buy_property(states_avenue)

    assert arvind_fx.cash == 360
    assert states_avenue in arvind_fx.player_portfolio

    arvind_fx.cash = 10
    arvind_fx.buy_property(st_charles_place)

    assert arvind_fx.cash == 10
    assert st_charles_place not in arvind_fx.player_portfolio


@pytest.mark.parametrize("current_tile, expected_current_tile, expected_cash", [
    (0, 12, 200),
    (28, 0, 200),
    (39, 11, 400)
])
def test_move(arvind_fx, pennsylvania_railroad, st_james_place, current_tile, expected_current_tile,
              expected_cash):
    arvind_fx.tile_no = current_tile
    arvind_fx.move(12)
    assert arvind_fx.tile_no == expected_current_tile
    assert arvind_fx.cash == expected_cash
    assert arvind_fx.tile_no < 39


@pytest.mark.parametrize("destination, collect_go_cash_flag, expected_destination, expected_cash", [
    ("states_avenue", True, "states_avenue", 400),
    ("states_avenue", False, "states_avenue", 200),
])
def test_move_to(arvind_fx, states_avenue, destination, expected_cash, expected_destination, collect_go_cash_flag,
                 request):
    input_destination = request.getfixturevalue(destination)
    expected_destination_value = request.getfixturevalue(expected_destination)
    arvind_fx.move_to(input_destination, collect_go_cash_flag=collect_go_cash_flag)
    assert arvind_fx.tile_no == expected_destination_value.tile_no
    assert arvind_fx.cash == expected_cash


def test_move_to_default_collect_go_cash_flag(arvind_fx, states_avenue):
    arvind_fx.move_to(states_avenue)
    assert arvind_fx.tile_no == states_avenue.tile_no
    assert arvind_fx.cash == 400


def test_pay_rent(arvind_fx, arun_fx):
    arvind_fx.pay_rent(arun_fx, 20)
    assert arvind_fx.cash == 180
    assert arun_fx.cash == 220

def test_pay_rent_color_set(arvind_fx, arun_fx, virginia_avenue, states_avenue, st_charles_place):
    arvind_fx.tile_no = 14
    arun_fx.player_portfolio.append(virginia_avenue)
    arun_fx.player_portfolio.append(states_avenue)
    arun_fx.player_portfolio.append(st_charles_place)
    arvind_fx.pay_rent(arun_fx, virginia_avenue.rent)
    assert arvind_fx.cash == 176
    assert arun_fx.cash == 224

@pytest.mark.parametrize("input_amount, expected_cash_1, expected_cash_2", [
    (100, 300, 100),
    (-50, 150, 250)
])
def test_transact_with_one_player(arvind_fx, arun_fx, input_amount, expected_cash_1, expected_cash_2):
    arvind_fx.player_transaction(arun_fx, input_amount)
    assert arvind_fx.cash == expected_cash_1
    assert arun_fx.cash == expected_cash_2


@pytest.mark.parametrize("input_amount, expected_cash_1, expected_cash_2, expected_cash_3, expected_cash_4", [
    (10, 230, 190, 190, 190),
     (-50, 50, 250, 250, 250)
])
def test_transact_with_multiple_players(arvind_fx, arun_fx, adityam_fx, padma_fx, input_amount, expected_cash_1, expected_cash_2, expected_cash_3, expected_cash_4):
    player_list = [arun_fx, adityam_fx, padma_fx]
    for player in player_list:
        arvind_fx.player_transaction(player, input_amount)
    assert arvind_fx.cash == expected_cash_1
    assert arun_fx.cash == expected_cash_2
    assert adityam_fx.cash == expected_cash_3
    assert padma_fx.cash == expected_cash_4


@pytest.mark.parametrize("input_amount, expected",[
    (100, 300),
    (-100, 100)
])
def test_bank_transaction(arvind_fx, input_amount, expected):
    arvind_fx.bank_transaction(input_amount)
    assert arvind_fx.cash == expected
