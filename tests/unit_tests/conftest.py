import json
from pathlib import Path

import pytest

from Player import Player
from Property import Property
from TileIterators import TileList, TileDict
from chance_tiles_data import chance_7, chance_22, chance_36
from special_tiles_data import go


@pytest.fixture
def property_rent_data():
    property_rent_data_file = Path(Path.cwd() / "property_rent_data.json")
    with open(property_rent_data_file) as f:
        property_rent_data = json.load(f)
        return property_rent_data

@pytest.fixture
def electric_company(property_rent_data):
    return Property(12, "Electric Company", 150, property_rent_data["Electric Company"]["Rent"])

@pytest.fixture
def chance_7_fx():
    return chance_7

@pytest.fixture
def chance_22_fx():
    return chance_22

@pytest.fixture
def chance_36_fx():
    return chance_36

@pytest.fixture
def go_fx():
    return go

@pytest.fixture
def st_james_place_fx():
    return st_james_place

@pytest.fixture
def states_avenue_fx():
    return states_avenue


@pytest.fixture
def st_charles_place_fx():
    return st_charles_place


@pytest.fixture
def virginia_avenue_fx():
    return virginia_avenue


@pytest.fixture
def pennsylvania_railroad_fx():
    return pennsylvania_railroad


@pytest.fixture
def property_list(states_avenue_fx, st_charles_place_fx, pennsylvania_railroad_fx, virginia_avenue_fx):
    ls = TileList([states_avenue_fx, st_charles_place_fx, pennsylvania_railroad_fx, virginia_avenue_fx])
    return ls


@pytest.fixture
def arvind_fx():
    arvind = Player("Arvind", 200)
    return arvind


@pytest.fixture
def arun_fx():
    arun = Player("Arun", 200)
    return arun


@pytest.fixture
def adityam_fx():
    adityam = Player("Adityam", 200)
    return adityam


@pytest.fixture
def padma_fx():
    padma = Player("Padma", 200)
    return padma


@pytest.fixture
def sree_fx():
    sree = Player("Sree", 200)
    return sree

@pytest.fixture
def property_dict(states_avenue_fx, st_charles_place_fx, pennsylvania_railroad_fx, virginia_avenue_fx, arvind_fx,
                  arun_fx):
    return TileDict({
        states_avenue_fx: arvind_fx,
        st_charles_place_fx: arun_fx,
        pennsylvania_railroad_fx: arvind_fx,
        virginia_avenue_fx: arun_fx
    })