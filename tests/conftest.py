import json
from pathlib import Path

import pytest

from Player import Player
from Property import Property
from Railroad import Railroad
from TileIterators import TileList, TileDict
from Utility import Utility
from chance_tiles_data import chance_7, chance_22, chance_36
from special_tiles_data import go


@pytest.fixture
def property_rent_data():
    property_rent_data_file = Path(Path.cwd() / "property_rent_data.json")
    with open(property_rent_data_file) as f:
        property_rent_data = json.load(f)
        return property_rent_data


@pytest.fixture
def reading_railroad(property_rent_data):
    return Railroad(5, "Reading Railroad", 200, property_rent_data["Reading Railroad"]["Rent"], "Railroad")

@pytest.fixture
def bo_railroad(property_rent_data):
    return Railroad(25, "B & O Railroad", 200, property_rent_data["B & O Railroad"]["Rent"], "Railroad")

@pytest.fixture
def short_line_railroad(property_rent_data):
    return Railroad(35, "Short Line", 200, property_rent_data["Short Line"]["Rent"], "Railroad")

@pytest.fixture
def pennsylvania_railroad(property_rent_data):
    return Railroad(15, "Pennsylvania Railroad", 200, property_rent_data["Pennsylvania Railroad"]["Rent"], "Railroad")

@pytest.fixture
def electric_company(property_rent_data):
    return Utility(12, "Electric Company", 150, property_rent_data["Electric Company"]["Rent"], "Utility")

@pytest.fixture
def water_works(property_rent_data):
    return Utility(28, "Water Works", 150, property_rent_data["Water Works"]["Rent"], "Utility")


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
def st_james_place(property_rent_data):
    return Property(16, "St. James Place", 180, property_rent_data["St. James Place"]["Rent"], "Orange", 100)

@pytest.fixture
def states_avenue(property_rent_data):
    return Property(13, "States Avenue", 140, property_rent_data["States Avenue"]["Rent"], "Pink", 100)


@pytest.fixture
def st_charles_place(property_rent_data):
    return Property(11, "St. Charles Place", 140, property_rent_data["St. Charles Place"]["Rent"], "Pink", 100)


@pytest.fixture
def virginia_avenue(property_rent_data):
    return Property(14, "Virginia Avenue", 160, property_rent_data["Virginia Avenue"]["Rent"], "Pink", 100)

@pytest.fixture
def property_list(states_avenue, st_charles_place, pennsylvania_railroad, virginia_avenue):
    ls = TileList([states_avenue, st_charles_place, pennsylvania_railroad, virginia_avenue])
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
def property_dict(states_avenue, st_charles_place, pennsylvania_railroad, virginia_avenue, arvind_fx,
                  arun_fx):
    return TileDict({
        states_avenue: arvind_fx,
        st_charles_place: arun_fx,
        pennsylvania_railroad: arvind_fx,
        virginia_avenue: arun_fx
    })