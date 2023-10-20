import pytest

from Player import Player
from errors import InsufficientFundsError, CannotBuildHouseError, CannotSellHouseError


def test_init_default_values():
    arvind = Player("Arvind")

    assert arvind.cash == 200
    assert arvind.networth == 0
    assert arvind.tile_no == 0


def test_init_correct_values():
    arvind = Player("Arvind", 500)

    assert arvind.name == "Arvind"
    assert arvind.cash == 500


def test_buy_asset(states_avenue, arvind, st_charles_place):
    arvind.cash = 500
    arvind.buy_asset(states_avenue)

    assert arvind.cash == 360
    assert states_avenue in arvind.player_portfolio

    arvind.cash = 10
    with pytest.raises(InsufficientFundsError):
        arvind.buy_asset(st_charles_place)

    assert arvind.cash == 10
    assert st_charles_place not in arvind.player_portfolio


def test_buy_asset_one_railroad(arvind, pennsylvania_railroad):
    arvind.buy_asset(pennsylvania_railroad)
    assert arvind.cash == 0
    assert pennsylvania_railroad in arvind.player_portfolio
    assert arvind.railroads_owned == 1


def test_buy_asset_one_utility(arvind, electric_company):
    arvind.buy_asset(electric_company)
    assert arvind.cash == 50
    assert electric_company in arvind.player_portfolio
    assert arvind.utilities_owned == 1


def test_buy_asset_multiple_utilities(arvind, electric_company, water_works):
    arvind.cash = 500
    arvind.buy_asset(electric_company)
    arvind.buy_asset(water_works)

    assert arvind.cash == 200
    assert electric_company in arvind.player_portfolio
    assert water_works in arvind.player_portfolio
    assert arvind.utilities_owned == 2

    arvind.buy_asset(electric_company)
    assert arvind.utilities_owned == 2


def test_buy_asset_multiple_railroads(arvind, pennsylvania_railroad, bo_railroad, reading_railroad,
                               short_line_railroad):
    arvind.cash = 1500
    arvind.buy_asset(pennsylvania_railroad)
    arvind.buy_asset(bo_railroad)
    arvind.buy_asset(reading_railroad)
    arvind.buy_asset(short_line_railroad)

    assert arvind.cash == 700
    assert pennsylvania_railroad in arvind.player_portfolio
    assert bo_railroad in arvind.player_portfolio
    assert reading_railroad in arvind.player_portfolio
    assert short_line_railroad in arvind.player_portfolio
    assert arvind.railroads_owned == 4

    arvind.buy_asset(pennsylvania_railroad)
    assert arvind.railroads_owned == 4


@pytest.mark.parametrize("current_tile, expected_current_tile, expected_cash", [
    (0, 12, 200),
    (28, 0, 200),
    (39, 11, 400)
])
def test_move(arvind, pennsylvania_railroad, st_james_place, current_tile, expected_current_tile,
              expected_cash):
    arvind.tile_no = current_tile
    arvind.move(12)
    assert arvind.tile_no == expected_current_tile
    assert arvind.cash == expected_cash
    assert arvind.tile_no < 39

@pytest.mark.parametrize("current_tile, expected_tile",[
    (15, 12),
    (0, 37)
])
def test_move_back(arvind, pennsylvania_railroad, electric_company, current_tile, expected_tile):
    arvind.tile_no = current_tile
    arvind.move(-3)
    assert arvind.tile_no == expected_tile
    assert arvind.tile_no < 39

@pytest.mark.parametrize("destination, collect_go_cash_flag, expected_destination, expected_cash", [
    ("states_avenue", True, "states_avenue", 400),
    ("states_avenue", False, "states_avenue", 200),
])
def test_move_to(arvind, states_avenue, destination, expected_cash, expected_destination, collect_go_cash_flag,
                 request):
    input_destination = request.getfixturevalue(destination)
    expected_destination_value = request.getfixturevalue(expected_destination)
    arvind.move_to(input_destination.tile_no, collect_go_cash_flag=collect_go_cash_flag)
    assert arvind.tile_no == expected_destination_value.tile_no
    assert arvind.cash == expected_cash


def test_move_to_default_collect_go_cash_flag(arvind, states_avenue):
    arvind.move_to(states_avenue.tile_no)
    assert arvind.tile_no == states_avenue.tile_no
    assert arvind.cash == 400


def test_pay_rent(arvind, arun):
    arvind.pay_rent(arun, 20)
    assert arvind.cash == 180
    assert arun.cash == 220


def test_pay_rent_color_set(arvind, arun, virginia_avenue, states_avenue, st_charles_place):
    arvind.tile_no = 14
    arun.player_portfolio.append(virginia_avenue)
    arun.player_portfolio.append(states_avenue)
    arun.player_portfolio.append(st_charles_place)
    virginia_avenue._color_set = True
    arvind.pay_rent(arun, virginia_avenue.rent)
    assert arvind.cash == 176
    assert arun.cash == 224


@pytest.mark.parametrize("input_amount, expected_cash_1, expected_cash_2", [
    (100, 300, 100),
    (-50, 150, 250)
])
def test_transact_with_one_player(arvind, arun, input_amount, expected_cash_1, expected_cash_2):
    arvind.player_transaction(arun, input_amount)
    assert arvind.cash == expected_cash_1
    assert arun.cash == expected_cash_2


@pytest.mark.parametrize("input_amount, expected_cash_1, expected_cash_2, expected_cash_3, expected_cash_4", [
    (10, 230, 190, 190, 190),
    (-50, 50, 250, 250, 250)
])
def test_transact_with_multiple_players(arvind, arun, adityam, padma, input_amount, expected_cash_1, expected_cash_2,
                                        expected_cash_3, expected_cash_4):
    player_list = [arun, adityam, padma]
    for player in player_list:
        arvind.player_transaction(player, input_amount)
    assert arvind.cash == expected_cash_1
    assert arun.cash == expected_cash_2
    assert adityam.cash == expected_cash_3
    assert padma.cash == expected_cash_4


@pytest.mark.parametrize("input_amount, expected", [
    (100, 300),
    (-100, 100)
])
def test_bank_transaction(arvind, input_amount, expected):
    arvind.bank_transaction(input_amount)
    assert arvind.cash == expected


def test_build_house_true(arvind, st_charles_place, mocker):
    arvind._player_portfolio.append(st_charles_place)
    mocker.patch('Player.check_player_has_color_set', return_value=True)
    mocker.patch('Player.check_property_can_be_developed', return_value=True)
    arvind.build_house(st_charles_place)
    assert st_charles_place._houses == 1
    assert arvind.cash == 100


def test_build_house_false(arvind, st_charles_place, mocker):
    mocker.patch('Player.check_player_has_color_set', return_value=False)
    mocker.patch('Player.check_property_can_be_developed', return_value=True)
    with pytest.raises(CannotBuildHouseError):
        arvind.build_house(st_charles_place)
    assert st_charles_place._houses == 0
    assert arvind.cash == 200


def test_build_hotel(mocker, arvind, st_charles_place):
    mocker.patch('Player.check_can_build_hotel', return_value=True)
    arvind.build_hotel(st_charles_place)
    assert st_charles_place._hotel == True


def test_pay_jail_fine(arvind):
    arvind.pay_jail_fine()
    assert arvind.cash == 150

def test_try_jail_double_throw_double(arvind, mocker):
    arvind.in_jail = True
    mocker.patch.object(arvind, 'throw_one_dice', return_value=1)
    arvind.try_jail_double_throw()
    assert arvind.in_jail == False

def test_try_jail_double_throw_not_double(arvind, mocker):
    arvind.in_jail = True
    mock = mocker.patch.object(arvind, 'throw_one_dice', side_effect=[1, 2])
    arvind.try_jail_double_throw()
    assert arvind.in_jail == True
    mock.assert_called()

def test_try_jail_double_throw_three_tries(arvind, mocker):
    arvind.in_jail = True
    arvind.jail_throw_counter = 2
    mock = mocker.patch.object(arvind, 'throw_one_dice', side_effect=[1, 2])
    arvind.try_jail_double_throw()
    assert arvind.in_jail == False
    mock.assert_called()

def test_get_out_of_jail_free(arvind):
    arvind.in_jail = True
    arvind.get_out_of_jail_free_card = 1
    arvind.get_out_of_jail_free()
    assert arvind.get_out_of_jail_free_card == 0
    assert arvind.in_jail == False

def test_sell_houses_1(arvind, st_charles_place):
    """
    Sell houses when there is a hotel.
    """
    st_charles_place._hotel = True
    st_charles_place._houses = 1

    with pytest.raises(CannotSellHouseError):
        arvind.sell_houses(st_charles_place, 1)

def test_sell_houses_2(arvind, st_charles_place):
    """
    Sell houses when there is no hotel.
    """
    st_charles_place._houses = 3
    st_charles_place.owner = arvind
    arvind.player_portfolio.append(st_charles_place)
    arvind.sell_houses(st_charles_place, 2)
    assert arvind.cash == 300
    assert st_charles_place._houses == 1

