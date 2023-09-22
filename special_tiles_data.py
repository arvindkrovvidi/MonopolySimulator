from ChanceTile import ChanceTile
from SpecialTiles import SpecialTiles
from TileIterators import TileList

go = SpecialTiles(0, "Go")
jail = SpecialTiles(30, "Jail")
go_to_jail = SpecialTiles(10, "Go to jail")
free_parking = SpecialTiles(20, "Free parking")
chance_7 = ChanceTile(name="Chance", tile_no=7)
chance_22 = ChanceTile(name="Chance", tile_no=22)
chance_36 = ChanceTile(name="Chance", tile_no=36)

all_special_tiles_list = TileList([go, jail, go_to_jail, free_parking, chance_7, chance_22, chance_36])