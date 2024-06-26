import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
import pytest

from Player import Player
from TileIterators import TileList, TileDict
from Tiles.ChanceTile import ChanceTile
from Tiles.CommunityChestTile import CommunityChestTile
from Tiles.Jail import Jail
from Tiles.Property import Property
from Tiles.Railroad import Railroad
from Tiles.Utility import Utility
from Tiles.SpecialTiles import SpecialTiles
from Tiles.FreeParkingTile import FreeParkingTile
from Board import ANSI_COLOR_CODES
from Tiles.IncomeTaxTile import IncomeTaxTile
from Tiles.LuxuryTaxTile import LuxuryTaxTile

@pytest.fixture
def property_rent_data():
    property_rent_data_file =  Path(__file__).resolve().parent.parent / "Tiles_data" / "property_rent_data.json"
    with open(property_rent_data_file) as f:
        property_rent_data = json.load(f)
        return property_rent_data

@pytest.fixture
def free_parking_tile():
    return FreeParkingTile(20, "Free parking")
@pytest.fixture
def go_to_jail():
    return FreeParkingTile(20, "Free parking")
@pytest.fixture
def jail():
    return Jail(10, "Jail/Just visiting")
@pytest.fixture
def income_tax():
    return IncomeTaxTile(name="Income Tax", tile_no=4)

@pytest.fixture
def luxury_tax():
    return LuxuryTaxTile(name="Luxury Tax", tile_no=38)

@pytest.fixture
def all_tiles_list(go, jail, income_tax, luxury_tax, free_parking_tile, states_avenue, st_charles_place, st_james_place, virginia_avenue, pennsylvania_railroad, bo_railroad, reading_railroad, short_line_railroad, electric_company, water_works, chance_7, chance_36, chance_22, chest_2):
    return TileList([go, jail, income_tax, luxury_tax, free_parking_tile, states_avenue, st_charles_place, st_james_place, virginia_avenue, pennsylvania_railroad, bo_railroad, reading_railroad, short_line_railroad, electric_company, water_works, chance_7, chance_36, chance_22, chest_2])

@pytest.fixture
def reading_railroad(property_rent_data):
    return Railroad(5, "Reading Railroad", 200, property_rent_data["Reading Railroad"]["Rent"], "Railroad", ANSI_COLOR_CODES["WHITE"])

@pytest.fixture
def bo_railroad(property_rent_data):
    return Railroad(25, "B & O Railroad", 200, property_rent_data["B & O Railroad"]["Rent"], "Railroad", ANSI_COLOR_CODES["WHITE"])

@pytest.fixture
def short_line_railroad(property_rent_data):
    return Railroad(35, "Short Line", 200, property_rent_data["Short Line"]["Rent"], "Railroad", ANSI_COLOR_CODES["WHITE"])

@pytest.fixture
def pennsylvania_railroad(property_rent_data):
    return Railroad(15, "Pennsylvania Railroad", 200, property_rent_data["Pennsylvania Railroad"]["Rent"], "Railroad", ANSI_COLOR_CODES["WHITE"])

@pytest.fixture
def electric_company(property_rent_data):
    return Utility(12, "Electric Company", 150, None, "Utility", ANSI_COLOR_CODES["WHITE"])

@pytest.fixture
def water_works(property_rent_data):
    return Utility(28, "Water Works", 150, None, "Utility", ANSI_COLOR_CODES["WHITE"])


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
def chest_2():
    return CommunityChestTile('Community Chest', 2)

@pytest.fixture
def go():
    return SpecialTiles(0, 'Go')

@pytest.fixture
def jail():
    return Jail(10, "Jail/Just visiting")

@pytest.fixture
def st_james_place(property_rent_data):
    return Property(16, "St. James Place", 180, property_rent_data["St. James Place"]["Rent"], "Orange", 100, ANSI_COLOR_CODES["ORANGE"])

@pytest.fixture
def tennessee_avenue(property_rent_data):
    return Property(16, "Tennessee Avenue", 180, property_rent_data["Tennessee Avenue"]["Rent"], "Orange", 100, ANSI_COLOR_CODES["ORANGE"])

@pytest.fixture
def new_york_avenue(property_rent_data):
    return Property(16, "New York Avenue", 200, property_rent_data["New York Avenue"]["Rent"], "Orange", 100, ANSI_COLOR_CODES["ORANGE"])

@pytest.fixture
def states_avenue(property_rent_data):
    return Property(13, "States Avenue", 140, property_rent_data["States Avenue"]["Rent"], "Pink", 100, ANSI_COLOR_CODES["PINK"])


@pytest.fixture
def st_charles_place(property_rent_data):
    return Property(11, "St. Charles Place", 140, property_rent_data["St. Charles Place"]["Rent"], "Pink", 100, ANSI_COLOR_CODES["PINK"])


@pytest.fixture
def virginia_avenue(property_rent_data):
    return Property(14, "Virginia Avenue", 160, property_rent_data["Virginia Avenue"]["Rent"], "Pink", 100, ANSI_COLOR_CODES["PINK"])

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