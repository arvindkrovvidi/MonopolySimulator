import pytest
from Player_data import arvind, arun
from utils import calculate_networth, find_winner
from Player import Player


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
    arvind_fx.net_worth = 150
    arun_fx.net_worth = 300
    assert find_winner([arvind_fx, arun_fx]) == arun_fx
    arvind_fx.net_worth = 300
    arun_fx.net_worth = 150
    assert find_winner([arvind_fx, arun_fx]) == arvind_fx


