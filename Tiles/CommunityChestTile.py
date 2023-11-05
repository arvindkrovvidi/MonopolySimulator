from Tiles.Property import Property
from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile
from Tiles_data.special_tiles_data import go
from utils import printing_and_logging


class CommunityChestTile(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

    def execute(self, player, _card_no: int, **kwargs) -> None:
        """
        Main function that executes chance tile cards based on card number.
        :param player: Player who is picking up the chance card.
        :param _card_no: The card number that the player picks. Ranges between 1 and 16.
        """
        printing_and_logging(f'{player} picked community chest card number {_card_no}')
        if _card_no == 1:
            printing_and_logging(f'Advance to Go (Collect $200)')
            player.move_to(go.tile_no, collect_go_cash_flag=True)
            player.bank_transaction(200)
        if _card_no == 2:
            printing_and_logging(f'Bank error in your favor. Collect $200')
            player.bank_transaction(200)
        if _card_no == 3:
            printing_and_logging(f'Doctor’s fee. Pay $50')
            player.bank_transaction(-50)
        if _card_no == 4:
            printing_and_logging(f'From sale of stock you get $50')
            player.bank_transaction(50)
        if _card_no == 5:
            printing_and_logging(f'Get Out of Jail Free')
            player.get_out_of_jail_free_card += 1
        if _card_no == 6:
            printing_and_logging(f'Go to Jail. Go directly to jail, do not pass Go, do not collect $200')
            player.move_to(10, collect_go_cash_flag=False)
        if _card_no == 7:
            printing_and_logging(f'Holiday fund matures. Receive $100')
            player.bank_transaction(100)
        if _card_no == 8:
            printing_and_logging(f'Income tax refund. Collect $20')
            player.bank_transaction(20)
        if _card_no == 9:
            printing_and_logging(f'It is your birthday. Collect $10 from every player')
            execute_chest_9(player, kwargs['all_players_list'])
        if _card_no == 10:
            printing_and_logging(f'Life insurance matures. Collect $100')
            player.bank_transaction(100)
        if _card_no == 11:
            printing_and_logging(f'Pay hospital fees of $100')
            player.bank_transaction(-100)
        if _card_no == 12:
            printing_and_logging(f'Pay school fees of $50')
            player.bank_transaction(-50)
        if _card_no == 13:
            printing_and_logging(f'Receive $25 consultancy fee')
            player.bank_transaction(25)
        if _card_no == 14:
            printing_and_logging(f'You are assessed for street repair. $40 per house. $115 per hotel')
            execute_chest_14(player)
        if _card_no == 15:
            printing_and_logging(f'You have won second prize in a beauty contest. Collect $10')
            player.bank_transaction(10)
        if _card_no == 16:
            printing_and_logging(f'You inherit $100')
            player.bank_transaction(100)

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