from Tile import Property
from TileIterators import TileList, TileDict

mediterranean_avenue = Property(1, "Mediterranean Avenue", 60, 2)
baltic_avenue = Property(3, 'Baltic Avenue', 60, 4)
reading_railroad = Property(5, "Reading Railroad", 200, 25)
oriental_avenue = Property(6, "Oriental Avenue", 100, 6)
vermont_avenue = Property(8, "Vermont Avenue", 100, 6)
connecticut_avenue = Property(9, "Connecticut Avenue", 120, 8)
electric_company = Property(12, "Electric Company", 150, 4)
st_charles_place = Property(11, "St. Charles Place", 140, 10)
states_avenue = Property(13, "States Avenue", 140, 10)
virginia_avenue = Property(14, "Virginia Avenue", 160, 12)
pennsylvania_railroad = Property(15, "Pennsylvania Railroad", 200, 25)
st_james_place = Property(16, "St. James Place", 180, 14)
tennessee_avenue = Property(18, "Tennessee Avenue", 180, 14)
new_york_avenue = Property(19, "New York Avenue", 200, 16)
kentucky_avenue = Property(21, "Kentucky Avenue", 220, 18)
indiana_avenue = Property(23, "Indiana Avenue", 220, 18)
illinois_avenue = Property(24, "Illinois Avenue", 240, 20)
bo_railroad = Property(25, "B & O Railroad", 200, 25)
atlantic_avenue = Property(26, "Atlantic Avenue", 260, 22)
ventnor_avenue = Property(27, "Ventnor Avenue", 260, 22)
water_works = Property(28, "Water Works", 150, 4)
marvin_gardens = Property(29, "Marvin Gardens", 280, 24)
pacific_avenue = Property(31, "Pacific Avenue", 300, 26)
north_carolina_avenue = Property(32, "North Carolina Avenue", 300, 26)
pennsylvania_avenue = Property(34, "Pennsylvania Avenue", 320, 28)
short_line = Property(36, "Short Line", 200, 25)
park_place = Property(38, "Park Place", 350, 35)
boardwalk = Property(39, "Boardwalk", 400, 50)

all_properties_list = TileList([mediterranean_avenue, baltic_avenue, reading_railroad, oriental_avenue, vermont_avenue, connecticut_avenue,
                                electric_company, st_charles_place, states_avenue, virginia_avenue, pennsylvania_railroad, st_james_place,
                                tennessee_avenue, new_york_avenue, kentucky_avenue, indiana_avenue, illinois_avenue, bo_railroad,
                                atlantic_avenue, ventnor_avenue, water_works, marvin_gardens, pacific_avenue, north_carolina_avenue,
                                pennsylvania_avenue, short_line, park_place, boardwalk])
property_tracker = TileDict({})
