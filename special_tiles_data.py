from IncomeTaxTile import IncomeTaxTile
from LuxuryTaxTile import LuxuryTaxTile
from SpecialTiles import SpecialTiles
from TileIterators import TileList

go = SpecialTiles(0, "Go")
jail = SpecialTiles(10, "Jail")
go_to_jail = SpecialTiles(30, "Go to jail")
free_parking = SpecialTiles(20, "Free parking")
income_tax = IncomeTaxTile(name="Income Tax", tile_no=4)
luxury_tax = LuxuryTaxTile(name="Luxury Tax", tile_no=38)

special_tiles_list = TileList([go, jail, go_to_jail, free_parking, income_tax, luxury_tax])