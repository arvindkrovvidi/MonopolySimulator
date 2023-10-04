from TileIterators import TileList
from Utility import Utility

electric_company = Utility(12, "Electric Company", 150, None, "Utility")
water_works = Utility(28, "Water Works", 150, None, "Utility")

utilities_list = TileList([electric_company, water_works])
