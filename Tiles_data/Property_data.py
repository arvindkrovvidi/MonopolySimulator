import json
from pathlib import Path

from TileIterators import TileList
from Tiles.Property import Property

current_directory = Path(__file__).resolve().parent
property_rent_data_file = current_directory / "property_rent_data.json"
with open(property_rent_data_file) as f:
    property_rent_data = json.load(f)

mediterranean_avenue = Property(1, "Mediterranean Avenue", 60, property_rent_data["Mediterranean Avenue"]["Rent"],  "Brown", 50)
baltic_avenue = Property(3, 'Baltic Avenue', 60, property_rent_data["Baltic Avenue"]["Rent"], "Brown", 50)
oriental_avenue = Property(6, "Oriental Avenue", 100, property_rent_data["Oriental Avenue"]["Rent"], "Light Blue", 50)
vermont_avenue = Property(8, "Vermont Avenue", 100, property_rent_data["Vermont Avenue"]["Rent"], "Light Blue", 50)
connecticut_avenue = Property(9, "Connecticut Avenue", 120, property_rent_data["Connecticut Avenue"]["Rent"], "Light Blue", 50)
st_charles_place = Property(11, "St. Charles Place", 140, property_rent_data["St. Charles Place"]["Rent"], "Pink", 100)
states_avenue = Property(13, "States Avenue", 140, property_rent_data["States Avenue"]["Rent"], "Pink", 100)
virginia_avenue = Property(14, "Virginia Avenue", 160, property_rent_data["Virginia Avenue"]["Rent"], "Pink", 100)
st_james_place = Property(16, "St. James Place", 180, property_rent_data["St. James Place"]["Rent"], "Orange", 100)
tennessee_avenue = Property(18, "Tennessee Avenue", 180, property_rent_data["Tennessee Avenue"]["Rent"], "Orange", 100)
new_york_avenue = Property(19, "New York Avenue", 200, property_rent_data["New York Avenue"]["Rent"], "Orange", 150)
kentucky_avenue = Property(21, "Kentucky Avenue", 220, property_rent_data["Kentucky Avenue"]["Rent"], "Red", 150)
indiana_avenue = Property(23, "Indiana Avenue", 220, property_rent_data["Indiana Avenue"]["Rent"], "Red", 150)
illinois_avenue = Property(24, "Illinois Avenue", 240, property_rent_data["Illinois Avenue"]["Rent"], "Red", 150)
atlantic_avenue = Property(26, "Atlantic Avenue", 260, property_rent_data["Atlantic Avenue"]["Rent"], "Yellow", 150)
ventnor_avenue = Property(27, "Ventnor Avenue", 260, property_rent_data["Ventnor Avenue"]["Rent"], "Yellow", 150)
marvin_gardens = Property(29, "Marvin Gardens", 280, property_rent_data["Marvin Gardens"]["Rent"], "Yellow", 150)
pacific_avenue = Property(31, "Pacific Avenue", 300, property_rent_data["Pacific Avenue"]["Rent"], "Green", 200)
north_carolina_avenue = Property(32, "North Carolina Avenue", 300, property_rent_data["North Carolina Avenue"]["Rent"], "Green", 200)
pennsylvania_avenue = Property(34, "Pennsylvania Avenue", 320, property_rent_data["Pennsylvania Avenue"]["Rent"], "Green", 200)
park_place = Property(37, "Park Place", 350, property_rent_data["Park Place"]["Rent"], "Blue", 200)
boardwalk = Property(39, "Boardwalk", 400, property_rent_data["Boardwalk"]["Rent"], "Blue", 200)

properties_list = TileList([mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue,
                            st_charles_place, states_avenue, virginia_avenue,
                            st_james_place,
                            tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue,
                            atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue,
                            pennsylvania_avenue, park_place, boardwalk])

property_data_by_color = {
    "Brown": TileList([mediterranean_avenue, baltic_avenue]),
    "Light Blue": TileList([oriental_avenue, vermont_avenue, connecticut_avenue]),
    "Pink": TileList([st_charles_place, states_avenue, virginia_avenue]),
    "Orange": TileList([st_james_place, tennessee_avenue, new_york_avenue]),
    "Red": TileList([kentucky_avenue, indiana_avenue, illinois_avenue]),
    "Yellow": TileList([atlantic_avenue, ventnor_avenue, marvin_gardens]),
    "Green": TileList([pacific_avenue, north_carolina_avenue, pennsylvania_avenue]),
    "Blue": TileList([park_place, boardwalk])
}