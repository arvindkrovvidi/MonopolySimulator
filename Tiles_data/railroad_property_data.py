from Board import ANSI_COLOR_CODES
from TileIterators import TileList
from Tiles.Railroad import Railroad
from Tiles_data.Property_data import property_rent_data

reading_railroad = Railroad(5, "Reading Railroad", 200, property_rent_data["Reading Railroad"]["Rent"], "Railroad", ANSI_COLOR_CODES["WHITE"])
pennsylvania_railroad = Railroad(15, "Pennsylvania Railroad", 200, property_rent_data["Pennsylvania Railroad"]["Rent"], "Railroad", ANSI_COLOR_CODES["WHITE"])
bo_railroad = Railroad(25, "B & O Railroad", 200, property_rent_data["B & O Railroad"]["Rent"], "Railroad", ANSI_COLOR_CODES["WHITE"])
short_line = Railroad(35, "Short Line", 200, property_rent_data["Short Line"]["Rent"], "Railroad", ANSI_COLOR_CODES["WHITE"])

railroad_properties_list = TileList([reading_railroad, bo_railroad, pennsylvania_railroad, short_line])
