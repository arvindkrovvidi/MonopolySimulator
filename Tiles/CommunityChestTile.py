from Player_data import all_players_list
from Tiles.Property import Property
from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile
from Tiles_data.special_tiles_data import go
from utils import printing_and_logging


class CommunityChestTile(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

    def execute(self, player, _card_no: int) -> None:
        """
        Main function that executes chance tile cards based on card number.
        :param player: Player who is picking up the chance card.
        :param _card_no: The card number that the player picks. Ranges between 1 and 16.
        """
        if _card_no == 1:
            player.move_to(go.tile_no)
            player.bank_transaction(200)
        if _card_no == 2:
            player.bank_transaction(200)
        if _card_no == 3:
            player.bank_transaction(-50)
        if _card_no == 4:
            player.bank_transaction(50)
        if _card_no == 5:
            player.get_out_of_jail_free_card += 1
        if _card_no == 6:
            player.move_to(10, collect_go_cash_flag=False)
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
            execute_chest_14(player)
        if _card_no == 15:
            player.bank_transaction(10)
        if _card_no == 16:
            player.bank_transaction(100)
        printing_and_logging(f'{player} played community chest card {_card_no}')

def execute_chest_14(player):
    """
    Execute chance card number 14. You are assessed for street repair. $40 per house. $115 per hotel.
    :param player: Player that picked the community chest card number 14
    :return: The total cost of repairs
    """
    houses = 0
    hotels = 0
    for each_property in player.player_portfolio:
        if type(each_property) == Property:
            houses += each_property._houses
            if each_property._hotel:
                hotels += 1
    repairs_cost = (40 * houses) + (115 * hotels)
    player.bank_transaction(-repairs_cost)

def execute_chest_9(player, players) -> None:
    """
    Execute community chest card number 9. It's your birthday. Collect $10 from every player.
    :param player: The player that picked the card. The player that collects the amount.
    :param players: The players paying the amount.
    """
    for each_player in players:
        player.player_transaction(each_player, 10)