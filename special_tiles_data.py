from ChanceTile import ChanceTile
from SpecialTiles import SpecialTiles
from TileIterators import TileList

go = SpecialTiles(0, "Go")
jail = SpecialTiles(30, "Jail")
go_to_jail = SpecialTiles(10, "Go to jail")
free_parking = SpecialTiles(20, "Free parking")

all_special_tiles_list = TileList([go, jail, go_to_jail, free_parking])