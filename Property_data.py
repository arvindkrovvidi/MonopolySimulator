import json
from pathlib import Path

from Property import Property
from TileIterators import TileList

property_rent_data_file = Path(Path.cwd() / "property_rent_data.json")
with open(property_rent_data_file) as f:
    property_rent_data = json.load(f)

mediterranean_avenue = Property(1, "Mediterranean Avenue", 60, property_rent_data["Mediterranean Avenue"]["Rent"])
baltic_avenue = Property(3, 'Baltic Avenue', 60, property_rent_data["Baltic Avenue"]["Rent"])
oriental_avenue = Property(6, "Oriental Avenue", 100, property_rent_data["Oriental Avenue"]["Rent"])
vermont_avenue = Property(8, "Vermont Avenue", 100, property_rent_data["Vermont Avenue"]["Rent"])
connecticut_avenue = Property(9, "Connecticut Avenue", 120, property_rent_data["Connecticut Avenue"]["Rent"])
st_charles_place = Property(11, "St. Charles Place", 140, property_rent_data["St. Charles Place"]["Rent"])
states_avenue = Property(13, "States Avenue", 140, property_rent_data["States Avenue"]["Rent"])
virginia_avenue = Property(14, "Virginia Avenue", 160, property_rent_data["Virginia Avenue"]["Rent"])
st_james_place = Property(16, "St. James Place", 180, property_rent_data["St. James Place"]["Rent"])
tennessee_avenue = Property(18, "Tennessee Avenue", 180, property_rent_data["Tennessee Avenue"]["Rent"])
new_york_avenue = Property(19, "New York Avenue", 200, property_rent_data["New York Avenue"]["Rent"])
kentucky_avenue = Property(21, "Kentucky Avenue", 220, property_rent_data["Kentucky Avenue"]["Rent"])
indiana_avenue = Property(23, "Indiana Avenue", 220, property_rent_data["Indiana Avenue"]["Rent"])
illinois_avenue = Property(24, "Illinois Avenue", 240, property_rent_data["Illinois Avenue"]["Rent"])
atlantic_avenue = Property(26, "Atlantic Avenue", 260, property_rent_data["Atlantic Avenue"]["Rent"])
ventnor_avenue = Property(27, "Ventnor Avenue", 260, property_rent_data["Ventnor Avenue"]["Rent"])
marvin_gardens = Property(29, "Marvin Gardens", 280, property_rent_data["Marvin Gardens"]["Rent"])
pacific_avenue = Property(31, "Pacific Avenue", 300, property_rent_data["Pacific Avenue"]["Rent"])
north_carolina_avenue = Property(32, "North Carolina Avenue", 300, property_rent_data["North Carolina Avenue"]["Rent"])
pennsylvania_avenue = Property(34, "Pennsylvania Avenue", 320, property_rent_data["Pennsylvania Avenue"]["Rent"])
park_place = Property(37, "Park Place", 350, property_rent_data["Park Place"]["Rent"])
boardwalk = Property(39, "Boardwalk", 400, property_rent_data["Boardwalk"]["Rent"])

properties_list = TileList([mediterranean_avenue, baltic_avenue, oriental_avenue, vermont_avenue, connecticut_avenue,
                            st_charles_place, states_avenue, virginia_avenue,
                            st_james_place,
                            tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue,
                            atlantic_avenue, ventnor_avenue, marvin_gardens, pacific_avenue, north_carolina_avenue,
                            pennsylvania_avenue, park_place, boardwalk])

