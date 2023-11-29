import pytest

from Player import Player
from errors import InvalidPropertyTypeError, PropertyNotFreeError, SelfOwnedPropertyError
from utils import calculate_networth, find_winner, get_positions, check_passing_go, check_player_has_color_set, \
    check_can_build_house_on_property, check_can_build_hotel_on_property, check_any_player_broke, set_color_set_value, \
    check_can_sell_house_on_property, check_can_sell_hotel_on_property, check_can_buy_asset, InsufficientFundsError, \
    get_display_options


def test_calculate_networth(st_charles_place, states_avenue, virginia_avenue,
                            pennsylvania_railroad):
    arvind = Player("Arvind", 1000)
    arvind.player_portfolio.append(st_charles_place)
    arvind.player_portfolio.append(states_avenue)
    arvind.player_portfolio.append(virginia_avenue)
    arvind.player_portfolio.append(pennsylvania_railroad)
    assert arvind.cash == 1000
    assert calculate_networth(arvind) == 1640


def test_find_winner(st_charles_place, states_avenue, virginia_avenue,
                     pennsylvania_railroad):
    arvind = Player("Arvind", 1000)
    arun = Player("Arun", 1000)
    arvind.networth = 150
    arun.networth = 300
    assert find_winner([arvind, arun])[0] == arun
    arvind.networth = 300
    arun.networth = 150
    assert find_winner([arvind, arun])[0] == arvind


@pytest.mark.parametrize("inputs, expected", [
    ((100, 200, 300, 400, 500),
     ([(1, 'Sree', 500), (2, 'Padma', 400), (3, 'Adityam', 300), (4, 'Arun', 200), (5, 'Arvind', 100)])),
    ((100, 200, 300, 500, 500),
     ([(1, 'Padma', 500), (1, 'Sree', 500), (3, 'Adityam', 300), (4, 'Arun', 200), (5, 'Arvind', 100)])),
    ((100, 100, 300, 500, 500),
     ([(1, 'Padma', 500), (1, 'Sree', 500), (3, 'Adityam', 300), (4, 'Arvind', 100), (4, 'Arun', 100)])),
    ((500, 500, 500, 500, 500),
     ([(1, 'Arvind', 500), (1, 'Arun', 500), (1, 'Adityam', 500), (1, 'Padma', 500), (1, 'Sree', 500)])),
    ((100, 500, 500, 500, 500),
     ([(1, 'Arun', 500), (1, 'Adityam', 500), (1, 'Padma', 500), (1, 'Sree', 500), (5, 'Arvind', 100)])),
    ((100, 100, 100, 500, 500),
     ([(1, 'Padma', 500), (1, 'Sree', 500), (3, 'Arvind', 100), (3, 'Arun', 100), (3, 'Adityam', 100)]))
])
def test_display_positions(inputs, expected, sree, padma, adityam, arun, arvind):
    arvind.networth = inputs[0]
    arun.networth = inputs[1]
    adityam.networth = inputs[2]
    padma.networth = inputs[3]
    sree.networth = inputs[4]

    actual = []
    for pos, win, nw in get_positions([arvind, arun, adityam, padma, sree]):
        actual.append((pos, str(win), nw))

    assert expected == actual


@pytest.mark.parametrize("current_tile, destination_tile, expected", [
    ("chance_7", "st_james_place", False),
    ("chance_22", "st_james_place", True),
    ("chance_36", "st_james_place", True)
])
def test_check_passing_go(arvind, st_james_place, request, current_tile, destination_tile, expected):
    current = request.getfixturevalue(current_tile)
    destination = request.getfixturevalue(destination_tile)
    arvind.tile_no = current.tile_no
    actual = check_passing_go(arvind, destination)

    assert actual == expected


def test_check_player_has_color_set_false(arvind, st_james_place, electric_company):
    arvind.player_portfolio.append(st_james_place)
    arvind.player_portfolio.append(electric_company)
    assert check_player_has_color_set(arvind, "Pink") == False
    assert check_player_has_color_set(arvind, "Utility") == False


def test_check_player_has_color_set_pink(arvind, st_charles_place, states_avenue, virginia_avenue):
    arvind.player_portfolio.append(st_charles_place)
    arvind.player_portfolio.append(states_avenue)
    arvind.player_portfolio.append(virginia_avenue)
    assert check_player_has_color_set(arvind, "Pink") == True


def test_check_player_has_color_set_railroad(arvind, pennsylvania_railroad, bo_railroad, reading_railroad,
                                             short_line_railroad):
    arvind.player_portfolio.append(pennsylvania_railroad)
    arvind.player_portfolio.append(bo_railroad)
    arvind.player_portfolio.append(reading_railroad)
    arvind.player_portfolio.append(short_line_railroad)
    assert check_player_has_color_set(arvind, "Railroad")


def test_check_player_has_color_set_utility(arvind, electric_company, water_works):
    arvind.player_portfolio.append(electric_company)
    arvind.player_portfolio.append(water_works)
    assert check_player_has_color_set(arvind, "Utility")


@pytest.mark.parametrize("property_1_house, property_2_house, property_3_house, expected_1, expected_2, expected_3", [
    (2, 2, 1, False, False, True),
    (2, 1, 1, False, True, True),
    (2, 2, 2, True, True, True)
])
def test_check_can_build_house_1(mocker, arvind, st_charles_place, states_avenue, virginia_avenue, property_1_house,
                                 property_2_house, property_3_house, expected_1, expected_2, expected_3, pennsylvania_railroad):
    arvind.cash = 500
    pennsylvania_railroad.owner = arvind
    st_charles_place.owner = arvind
    states_avenue.owner = arvind
    virginia_avenue.owner = arvind

    st_charles_place._houses = property_1_house
    states_avenue._houses = property_2_house
    virginia_avenue._houses = property_3_house

    mocker.patch('utils.check_player_has_color_set', return_value=True)

    assert check_can_build_house_on_property(arvind, st_charles_place) == expected_1
    assert check_can_build_house_on_property(arvind, states_avenue) == expected_2
    assert check_can_build_house_on_property(arvind, virginia_avenue) == expected_3

def test_check_can_build_house_2(arvind, pennsylvania_railroad, electric_company):
    """
    Test check_can_build_house_on_property when property is a railroad/utility
    """
    pennsylvania_railroad.owner = arvind
    electric_company.owner = arvind

    with pytest.raises(InvalidPropertyTypeError):
        check_can_build_house_on_property(arvind, pennsylvania_railroad)

    with pytest.raises(InvalidPropertyTypeError):
        check_can_build_house_on_property(arvind, electric_company)

@pytest.mark.parametrize("property_1_house, property_2_house, property_3_house, expected_1, expected_2, expected_3", [
    (4, 4, 3, False, False, False),
    (4, 4, 4, True, True, True)
])
def test_check_can_build_hotel_1(arvind, st_charles_place, states_avenue, virginia_avenue, property_1_house,
                                 property_2_house, property_3_house, expected_1, expected_2, expected_3, pennsylvania_railroad):
    pennsylvania_railroad.owner = arvind
    st_charles_place.owner = arvind
    states_avenue.owner = arvind
    virginia_avenue.owner = arvind
    st_charles_place._houses = property_1_house
    states_avenue._houses = property_2_house
    virginia_avenue._houses = property_3_house
    assert check_can_build_hotel_on_property(arvind, st_charles_place) == expected_1
    assert check_can_build_hotel_on_property(arvind, states_avenue) == expected_2
    assert check_can_build_hotel_on_property(arvind, virginia_avenue) == expected_3


@pytest.mark.parametrize("arvind_cash, arun_cash, padma_cash, adityam_cash, expected", [
    (100, 100, 100, 100, False),
    (100, -100, 100, 100, True),
    (-100, 100, 100, 100, True),
    (100, 100, 100, -100, True)
])
def test_check_any_player_broke(arvind, arun, padma, adityam, arvind_cash, arun_cash, adityam_cash, padma_cash,
                                expected):
    arvind.cash = arvind_cash
    arun.cash = arun_cash
    adityam.cash = adityam_cash
    padma.cash = padma_cash

    player_list = [arvind, arun, adityam, padma]
    assert check_any_player_broke(player_list) == expected


def test_set_color_set(arvind, st_charles_place, virginia_avenue, states_avenue):
    arvind.player_portfolio.append(states_avenue)
    arvind.player_portfolio.append(virginia_avenue)
    arvind.buy_asset(st_charles_place)

    set_color_set_value(arvind, st_charles_place)
    assert st_charles_place._color_set == True
    assert virginia_avenue._color_set == True
    assert states_avenue._color_set == True


def test_check_can_sell_house_1(arvind, pennsylvania_railroad):
    """
    Test check_can_sell_house_on_property when property is Railroad or Utility
    """
    pennsylvania_railroad.owner = arvind
    arvind.player_portfolio.append(pennsylvania_railroad)
    with pytest.raises(InvalidPropertyTypeError):
        check_can_sell_house_on_property(arvind, pennsylvania_railroad)


def test_check_can_sell_house_2(arvind, st_charles_place):
    """
    Test check_can_sell_house_on_property when property has hotel
    """
    st_charles_place._hotel = True
    arvind.player_portfolio.append(st_charles_place)
    st_charles_place.owner = arvind
    assert check_can_sell_house_on_property(arvind, st_charles_place) == False


@pytest.mark.parametrize("property_1_houses, property_2_houses, property_3_houses, expected", [
    (2, 2, 2, True),
    (1, 2, 2, False),
    (3, 2, 2, True)
])
def test_check_can_sell_house_3(arvind, st_charles_place, states_avenue, virginia_avenue, property_1_houses,
                                property_2_houses, property_3_houses, expected):
    """
    Test check_can_sell_house_on_property
    """
    st_charles_place._houses = property_1_houses
    states_avenue._houses = property_2_houses
    virginia_avenue._houses = property_3_houses
    arvind.player_portfolio.append(states_avenue)
    arvind.player_portfolio.append(st_charles_place)
    arvind.player_portfolio.append(virginia_avenue)
    states_avenue.owner = arvind
    st_charles_place.owner = arvind
    virginia_avenue.owner = arvind

    assert check_can_sell_house_on_property(arvind, st_charles_place) == expected


def test_check_can_sell_hotel_1(arvind, pennsylvania_railroad):
    """
    Test check_can_sell_hotel_on_property when asset is a railroad/utility
    """
    pennsylvania_railroad.owner = arvind
    arvind.player_portfolio.append(pennsylvania_railroad)

    with pytest.raises(InvalidPropertyTypeError):
        check_can_sell_hotel_on_property(arvind, pennsylvania_railroad)

    assert arvind.cash == 200


def test_check_can_sell_hotel_2(arvind, st_charles_place):
    """
    Test check_can_sell_hotel_on_property when there is a hotel on the property.
    """

    st_charles_place.owner = arvind
    arvind.player_portfolio.append(st_charles_place)
    st_charles_place._hotel = True

    assert check_can_sell_hotel_on_property(arvind, st_charles_place) == True


@pytest.mark.parametrize("asset", ["st_charles_place", "pennsylvania_railroad", "electric_company"])
def test_check_can_buy_asset_1(arvind, arun, asset, request):
    """
    Test check_can_buy_asset when asset is owned by someone else
    """
    asset = request.getfixturevalue(asset)
    arun.player_portfolio.append(asset)
    asset.owner = arun

    with pytest.raises(PropertyNotFreeError):
        check_can_buy_asset(arvind, asset)


@pytest.mark.parametrize("asset", ["st_charles_place", "pennsylvania_railroad", "electric_company"])
def test_check_can_buy_asset_2(arvind, asset, request):
    """
    Test check_can_buy_asset when asset is owned by the player trying to buy the asset.
    """
    asset = request.getfixturevalue(asset)
    arvind.player_portfolio.append(asset)
    asset.owner = arvind

    with pytest.raises(SelfOwnedPropertyError):
        check_can_buy_asset(arvind, asset)


@pytest.mark.parametrize("asset", ["st_charles_place", "pennsylvania_railroad", "electric_company"])
def test_check_can_buy_asset_3(arvind, asset, request):
    """
    Test check_can_buy_asset when player does not have sufficient funds to buy the asset.
    """
    arvind.cash = 0
    asset = request.getfixturevalue(asset)
    assert asset.owner is None

    with pytest.raises(InsufficientFundsError):
        check_can_buy_asset(arvind, asset)


@pytest.mark.parametrize("asset", ["st_charles_place", "pennsylvania_railroad", "electric_company"])
def test_check_can_buy_asset_4(arvind, asset, request):
    """
    Test check_can_buy_asset when all conditions are true for buying asset
    """
    arvind.cash = 300
    asset = request.getfixturevalue(asset)
    assert asset.owner is None

    assert check_can_buy_asset(arvind, asset) == True


def test_get_display_options():
    """
    Test get_display_options
    """
    options_list = ['Buy property', 'Buy house', 'Buy hotel', 'Sell house', 'Sell hotel']
    actual = get_display_options(options_list)
    expected = '[0] Buy property    [1] Buy house    [2] Buy hotel    [3] Sell house    [4] Sell hotel    '
    assert actual == expected