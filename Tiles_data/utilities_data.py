from Board import ANSI_COLOR_CODES
from TileIterators import TileList
from Tiles.Utility import Utility

electric_company = Utility(12, "Electric Company", 150, None, "Utility", ANSI_COLOR_CODES["WHITE"])
water_works = Utility(28, "Water Works", 150, None, "Utility", ANSI_COLOR_CODES["WHITE"])

utilities_list = TileList([electric_company, water_works])
