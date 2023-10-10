from TileIterators import TileList
from Tiles.FreeParkingTile import FreeParkingTile
from Tiles.IncomeTaxTile import IncomeTaxTile
from Tiles.Jail import Jail
from Tiles.LuxuryTaxTile import LuxuryTaxTile
from Tiles.SpecialTiles import SpecialTiles

go = SpecialTiles(0, "Go")
just_visiting_jail = SpecialTiles(10, "Just visiting")
free_parking = SpecialTiles(20, "Free parking")
income_tax = IncomeTaxTile(name="Income Tax", tile_no=4)
luxury_tax = LuxuryTaxTile(name="Luxury Tax", tile_no=38)
jail = Jail(30, "Go to jail")
special_tiles_list = TileList([go, just_visiting_jail, jail, free_parking, income_tax, luxury_tax])