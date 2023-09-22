from ChanceTile import ChanceTile
from CommunityChestTile import CommunityChestTile
from IncomeTaxTile import IncomeTaxTile
from LuxuryTaxTile import LuxuryTaxTile
from SpecialTiles import SpecialTiles
from TileIterators import TileList

go = SpecialTiles(0, "Go")
jail = SpecialTiles(10, "Jail")
go_to_jail = SpecialTiles(30, "Go to jail")
free_parking = SpecialTiles(20, "Free parking")
chance_7 = ChanceTile(name="Chance", tile_no=7)
chance_22 = ChanceTile(name="Chance", tile_no=22)
chance_36 = ChanceTile(name="Chance", tile_no=36)
community_chest_2 = CommunityChestTile(name="Community Chest", tile_no=2)
community_chest_17 = CommunityChestTile(name="Community Chest", tile_no=17)
community_chest_33 = CommunityChestTile(name="Community Chest", tile_no=33)
income_tax = IncomeTaxTile(name="Income Tax", tile_no=4)
luxury_tax = LuxuryTaxTile(name="Luxury Tax", tile_no=38)

all_special_tiles_list = TileList([go, jail, go_to_jail, free_parking, chance_7, chance_22, chance_36,
                                   community_chest_33, community_chest_2, community_chest_17,
                                   income_tax, luxury_tax])