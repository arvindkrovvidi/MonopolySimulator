import pytest

from Player import Player
from utils import calculate_networth, find_winner, get_positions, check_passing_go, check_player_has_color_set, \
    check_property_can_be_developed


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
    arvind.player_color_data[st_james_place.color] += 1
    arvind.player_color_data[electric_company.color] += 1
    assert check_player_has_color_set(arvind, "Pink") == False
    assert check_player_has_color_set(arvind, "Utility") == False

def test_check_player_has_color_set_pink(arvind, st_charles_place, states_avenue, virginia_avenue):
    arvind.player_portfolio.append(st_charles_place)
    arvind.player_portfolio.append(states_avenue)
    arvind.player_portfolio.append(virginia_avenue)
    arvind.player_color_data[st_charles_place.color] += 1
    arvind.player_color_data[states_avenue.color] += 1
    arvind.player_color_data[virginia_avenue.color] += 1
    assert check_player_has_color_set(arvind, "Pink") == True

def test_check_player_has_color_set_railroad(arvind, pennsylvania_railroad, bo_railroad, reading_railroad,
                                             short_line_railroad):
    arvind.player_portfolio.append(pennsylvania_railroad)
    arvind.player_portfolio.append(bo_railroad)
    arvind.player_portfolio.append(reading_railroad)
    arvind.player_portfolio.append(short_line_railroad)
    arvind.player_color_data[pennsylvania_railroad.color] += 1
    arvind.player_color_data[bo_railroad.color] += 1
    arvind.player_color_data[reading_railroad.color] += 1
    arvind.player_color_data[short_line_railroad.color] += 1
    assert check_player_has_color_set(arvind, "Railroad")

def test_check_player_has_color_set_utility(arvind, electric_company, water_works):
    arvind.player_portfolio.append(electric_company)
    arvind.player_portfolio.append(water_works)
    arvind.player_color_data[electric_company.color] += 1
    arvind.player_color_data[water_works.color] += 1
    assert check_player_has_color_set(arvind, "Utility")


@pytest.mark.parametrize("property_1_house, property_2_house, property_3_house, expected",[
    (2, 1, 1, False)
])
def test_check_property_can_be_developed_1(arvind, st_charles_place, states_avenue, virginia_avenue, property_1_house, property_2_house, property_3_house, expected):
    st_charles_place._houses = property_1_house
    states_avenue._houses = property_2_house
    virginia_avenue._houses = property_3_house

    assert check_property_can_be_developed(st_charles_place) == expected

@pytest.mark.parametrize("property_1_house, property_2_house, property_3_house, expected",[
    (2, 2, 2, False)
])
def test_check_property_can_be_developed_2(arvind, st_charles_place, states_avenue, virginia_avenue, property_1_house, property_2_house, property_3_house, expected):
    st_charles_place._houses = property_1_house
    states_avenue._houses = property_2_house
    virginia_avenue._houses = property_3_house

    assert check_property_can_be_developed(st_charles_place) == expected

@pytest.mark.parametrize("property_1_house, property_2_house, property_3_house, expected",[
    (2, 2, 1, False)
])
def test_check_property_can_be_developed_3(arvind, st_charles_place, states_avenue, virginia_avenue, property_1_house, property_2_house, property_3_house, expected):
    st_charles_place._houses = property_1_house
    states_avenue._houses = property_2_house
    virginia_avenue._houses = property_3_house

    assert check_property_can_be_developed(st_charles_place) == expected

