from Player import Player
import pytest
from PropertyIterators import PropertyList
def test_init_default_values():
    arvind = Player("Arvind")

    assert arvind.cash == 200
    assert arvind.networth == 0
    assert arvind.tile_no == 0

def test_init_correct_values():
    arvind = Player("Arvind", 500)

    assert arvind.name == "Arvind"
    assert arvind.cash == 500
