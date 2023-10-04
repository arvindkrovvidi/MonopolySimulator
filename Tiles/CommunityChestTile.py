from Player_data import all_players_list
from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile
from Tiles_data.special_tiles_data import go


class CommunityChestTile(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

    @staticmethod
    def execute(player, _card_no: int) -> None:
        """
        Main function that executes chance tile cards based on card number.
        :param player: Player who is picking up the chance card.
        :param _card_no: The card number that the player picks. Ranges between 1 and 16.
        """
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

def execute_chest_9(player, players) -> None:
    """
    Execute community chest card number 9. It's your birthday. Collect $10 from every player.
    :param player: The player that picked the card. The player that collects the amount.
    :param players: The players paying the amount.
    """
    for each_player in players:
        player.player_transaction(each_player, 10)