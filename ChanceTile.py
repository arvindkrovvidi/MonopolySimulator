from Property_data import boardwalk, illinois_avenue, st_charles_place, raiload_properties_list, property_tracker
from SpecialTiles import SpecialTiles
from Tile import Tile
from special_tiles_data import go
from utils import check_passing_go


class ChanceTile(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)


    @staticmethod
    def execute(player, _card_no):
        if _card_no == 1:
            player.move_to(boardwalk, collect_go_cash_flag=False)
        elif _card_no == 2:
            player.move_to(go, collect_go_cash_flag=False)
        elif _card_no == 3:
            player.move_to(illinois_avenue, collect_go_cash_flag=check_passing_go(player, illinois_avenue))
        elif _card_no == 4:
            player.move_to(st_charles_place, collect_go_cash_flag=check_passing_go(player, illinois_avenue))
        elif _card_no == 5:
            execute_chance_5(player, property_tracker)


def get_nearest_railroad(player):
    if player.tile_no == 7:
        nearest_railroad = raiload_properties_list[5]
    if player.tile_no == 22:
        nearest_railroad = raiload_properties_list[25]
    if player.tile_no == 36:
        nearest_railroad = raiload_properties_list[35]
    return nearest_railroad
def execute_chance_5(player, tracker):
    nearest_railroad = get_nearest_railroad(player)
    player.move_to(nearest_railroad, collect_go_cash_flag=False)
    if nearest_railroad not in tracker.keys():
        player.buy_property(nearest_railroad)
    else:
        landlord = tracker[nearest_railroad]
        player.pay_rent(landlord, nearest_railroad.rent*2)
