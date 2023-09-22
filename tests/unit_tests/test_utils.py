import pytest

from Player import Player
from utils import calculate_networth, find_winner, display_positions, check_passing_go


def test_calculate_networth(st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                            pennsylvania_railroad_fx):
    arvind_fx = Player("Arvind", 1000)
    arvind_fx.buy_property(st_charles_place_fx)
    arvind_fx.buy_property(states_avenue_fx)
    arvind_fx.buy_property(virginia_avenue_fx)
    arvind_fx.buy_property(pennsylvania_railroad_fx)
    assert calculate_networth(arvind_fx) == 1000


def test_find_winner(st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                     pennsylvania_railroad_fx):
    arvind_fx = Player("Arvind", 1000)
    arun_fx = Player("Arun", 1000)
    arvind_fx.networth = 150
    arun_fx.networth = 300
    assert find_winner([arvind_fx, arun_fx])[0] == arun_fx
    arvind_fx.networth = 300
    arun_fx.networth = 150
    assert find_winner([arvind_fx, arun_fx])[0] == arvind_fx


@pytest.mark.parametrize("inputs, expected", [
    ((100, 200, 300, 400, 500), ([(1, 'Sree', 500), (2, 'Padma', 400), (3, 'Adityam', 300), (4, 'Arun', 200), (5, 'Arvind', 100)])),
    ((100, 200, 300, 500, 500), ([(1, 'Padma', 500), (1, 'Sree', 500), (3, 'Adityam', 300), (4, 'Arun', 200), (5, 'Arvind', 100)])),
    ((100, 100, 300, 500, 500), ([(1, 'Padma', 500), (1, 'Sree', 500), (3, 'Adityam', 300), (4, 'Arvind', 100), (4, 'Arun', 100)])),
    ((500, 500, 500, 500, 500), ([(1, 'Arvind', 500), (1, 'Arun', 500), (1, 'Adityam', 500), (1, 'Padma', 500), (1, 'Sree', 500)])),
    ((100, 500, 500, 500, 500), ([(1, 'Arun', 500), (1, 'Adityam', 500), (1, 'Padma', 500), (1, 'Sree', 500), (5, 'Arvind', 100)])),
    ((100, 100, 100, 500, 500), ([(1, 'Padma', 500), (1, 'Sree', 500), (3, 'Arvind', 100), (3, 'Arun', 100), (3, 'Adityam', 100)]))
])
def test_display_positions(inputs, expected, sree_fx, padma_fx, adityam_fx, arun_fx, arvind_fx):
    arvind_fx.networth = inputs[0]
    arun_fx.networth = inputs[1]
    adityam_fx.networth = inputs[2]
    padma_fx.networth = inputs[3]
    sree_fx.networth = inputs[4]

    actual = []
    for pos, win, nw in display_positions([arvind_fx, arun_fx, adityam_fx, padma_fx, sree_fx]):
        actual.append((pos, str(win), nw))

    assert expected == actual


@pytest.mark.parametrize("current_tile, destination_tile, expected", [
    ("chance_7_fx", "st_james_place_fx", False),
    ("chance_22_fx", "st_james_place_fx", True),
    ("chance_36_fx", "st_james_place_fx", True)
])
def test_check_passing_go(arvind_fx, st_james_place_fx, request, current_tile, destination_tile, expected):
    current = request.getfixturevalue(current_tile)
    destination = request.getfixturevalue(destination_tile)
    arvind_fx.tile_no = current.tile_no
    actual = check_passing_go(arvind_fx, destination)

    assert actual == expected
