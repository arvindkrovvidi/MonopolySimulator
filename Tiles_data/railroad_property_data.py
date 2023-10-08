from TileIterators import TileList
from Tiles.Railroad import Railroad
from Tiles_data.Property_data import property_rent_data

reading_railroad = Railroad(5, "Reading Railroad", 200, property_rent_data["Reading Railroad"]["Rent"], "Railroad")
pennsylvania_railroad = Railroad(15, "Pennsylvania Railroad", 200, property_rent_data["Pennsylvania Railroad"]["Rent"], "Railroad")
bo_railroad = Railroad(25, "B & O Railroad", 200, property_rent_data["B & O Railroad"]["Rent"], "Railroad")
short_line = Railroad(35, "Short Line", 200, property_rent_data["Short Line"]["Rent"], "Railroad")

railroad_properties_list = TileList([reading_railroad, bo_railroad, pennsylvania_railroad, short_line])
