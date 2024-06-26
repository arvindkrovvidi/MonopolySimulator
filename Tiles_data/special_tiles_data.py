from TileIterators import TileList
from Tiles.FreeParkingTile import FreeParkingTile
from Tiles.GoToJail import GoToJail
from Tiles.IncomeTaxTile import IncomeTaxTile
from Tiles.Jail import Jail
from Tiles.LuxuryTaxTile import LuxuryTaxTile
from Tiles.SpecialTiles import SpecialTiles

go = SpecialTiles(0, "Go")
jail = Jail(10, "Jail/Just visiting")
free_parking = FreeParkingTile(20, "Free parking")
income_tax = IncomeTaxTile(name="Income Tax", tile_no=4)
luxury_tax = LuxuryTaxTile(name="Luxury Tax", tile_no=38)
go_to_jail = GoToJail(30, "Go to Jail")
special_tiles_list = TileList([go, jail, go_to_jail, free_parking, income_tax, luxury_tax])