from Player_data import all_players_list
from SpecialTiles import SpecialTiles
from Tile import Tile
from special_tiles_data import go


class CommunityChestTile(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

    @staticmethod
    def execute(player, _card_no):
        if _card_no == 1:
            player.move_to(go)
            player.bank_transaction(200)
        if _card_no == 2:
            player.bank_transaction(200)
        if _card_no == 3:
            player.bank_transaction(-50)
        if _card_no == 4:
            player.bank_transaction(50)
        if _card_no == 5:
            pass
        if _card_no == 6:
            pass
        if _card_no == 7:
            player.bank_transaction(100)
        if _card_no == 8:
            player.bank_transaction(20)
        if _card_no == 9:
            execute_chest_9(player, all_players_list)
        if _card_no == 10:
            player.bank_transaction(100)
        if _card_no == 11:
            player.bank_transaction(-100)
        if _card_no == 12:
            player.bank_transaction(-50)
        if _card_no == 13:
            player.bank_transaction(25)
        if _card_no == 14:
            pass
        if _card_no == 15:
            player.bank_transaction(10)
        if _card_no == 16:
            player.bank_transaction(100)

def execute_chest_9(player, players):
    for each_player in players:
        player.player_transaction(each_player, 10)