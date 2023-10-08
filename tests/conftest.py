import json
from pathlib import Path

import pytest

from Player import Player
from TileIterators import TileList, TileDict
from Tiles.ChanceTile import ChanceTile
from Tiles.Property import Property
from Tiles.Railroad import Railroad
from Tiles.Utility import Utility
from Tiles_data.special_tiles_data import go


# @pytest.fixture
# def property_data_by_color():
#     return {
#     "Brown": TileList([mediterranean_avenue, baltic_avenue]),
#     "Light Blue": TileList([oriental_avenue, vermont_avenue, connecticut_avenue]),
#     "Pink": TileList([st_charles_place, states_avenue, virginia_avenue]),
#     "Orange": TileList([st_james_place, tennessee_avenue, new_york_avenue]),
#     "Red": TileList([kentucky_avenue, indiana_avenue, illinois_avenue]),
#     "Yellow": TileList([atlantic_avenue, ventnor_avenue, marvin_gardens]),
#     "Green": TileList([pacific_avenue, north_carolina_avenue, pennsylvania_avenue]),
#     "Blue": TileList([park_place, boardwalk])
# }

@pytest.fixture
def property_rent_data():
    property_rent_data_file = Path(Path.cwd() / "Tiles_data" / "property_rent_data.json")
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
    return Utility(12, "Electric Company", 150, None, "Utility")

@pytest.fixture
def water_works(property_rent_data):
    return Utility(28, "Water Works", 150, None, "Utility")


@pytest.fixture
def chance_7():
    return ChanceTile(name="Chance", tile_no=7)

@pytest.fixture
def chance_22():
    return ChanceTile(name="Chance", tile_no=22)

@pytest.fixture
def chance_36():
    return ChanceTile(name="Chance", tile_no=36)

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
def property_data_by_color(states_avenue, st_charles_place, virginia_avenue):
    return {
        "Pink": TileList([virginia_avenue, states_avenue, st_charles_place])
    }

@pytest.fixture
def arvind():
    return Player("Arvind", 200)


@pytest.fixture
def arun():
    return Player("Arun", 200)


@pytest.fixture
def adityam():
    return Player("Adityam", 200)


@pytest.fixture
def padma():
    return Player("Padma", 200)


@pytest.fixture
def sree():
    return Player("Sree", 200)

@pytest.fixture
def property_dict(states_avenue, st_charles_place, pennsylvania_railroad, virginia_avenue, arvind,
                  arun):
    return TileDict({
        states_avenue: arvind,
        st_charles_place: arun,
        pennsylvania_railroad: arvind,
        virginia_avenue: arun
    })