from Property_data import property_rent_data
from TileIterators import TileList
from Utility import Utility

electric_company = Utility(12, "Electric Company", 150, property_rent_data["Electric Company"]["Rent"])
water_works = Utility(28, "Water Works", 150, property_rent_data["Water Works"]["Rent"])

utilities_list = TileList([electric_company, water_works])
