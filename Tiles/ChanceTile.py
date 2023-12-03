from Tiles.Property import Property
from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile
from Tiles_data.Property_data import boardwalk, illinois_avenue, st_charles_place
from Tiles_data.railroad_property_data import reading_railroad, railroad_properties_list
from Tiles_data.special_tiles_data import go
from Tiles_data.utilities_data import utilities_list
from config import printing_and_logging
from errors import InsufficientFundsError, PropertyNotFreeError
from utils import check_passing_go, check_can_buy_asset


class ChanceTile(SpecialTiles):
    def __init__(self, name, tile_no, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)


    def execute(self, player, _card_no, **kwargs):
        """
        Main function that executes chance tile cards based on card number.
        :param player: Player who is picking up the chance card.
        :param _card_no: The card number that the player picks. Ranges between 1 and 16.
        """
        printing_and_logging(f'{player} picked chance card number {_card_no}')
        if _card_no == 1:
            printing_and_logging(f'Advance to Boardwalk')
            player.move_to(boardwalk.tile_no, collect_go_cash_flag=False)
            return True
        elif _card_no == 2:
            printing_and_logging(f'Advance to Go(collect 200)')
            player.move_to(go.tile_no, collect_go_cash_flag=True)
            return True
        elif _card_no == 3:
            printing_and_logging(f'Advance to Illinois Avenue. If you pass Go, collect $200')
            player.move_to(illinois_avenue.tile_no, collect_go_cash_flag=check_passing_go(player, illinois_avenue))
            return True
        elif _card_no == 4:
            printing_and_logging(f'Advance to St. Charles Place. If you pass Go, collect $200')
            player.move_to(st_charles_place.tile_no, collect_go_cash_flag=check_passing_go(player, illinois_avenue))
            return True
        elif _card_no == 5 or _card_no == 6:
            printing_and_logging(f'Advance to the nearest Railroad. If unowned, you may buy it from the Bank. If owned, pay wonder twice the rental to which they are otherwise entitled')
            try:
                execute_chance_5(player)
            except InsufficientFundsError as e:
                printing_and_logging(f'{player} cannot buy {railroad_properties_list[player.tile_no]}')
                printing_and_logging(e.exc_message)
            except PropertyNotFreeError as e:
                printing_and_logging(e.exc_message)
            else:
                return True
        elif _card_no == 7:
            printing_and_logging(f'Advance token to nearest Utility. If unowned, you may buy it from the Bank. If owned, throw dice and pay owner a total ten times amount thrown.')
            try:
                execute_chance_7(player, kwargs['throw'])
            except InsufficientFundsError as e:
                printing_and_logging(f'{player} cannot buy {utilities_list[player.tile_no]}')
                printing_and_logging(e.exc_message)
            except PropertyNotFreeError as e:
                printing_and_logging(e.exc_message)
            else:
                return True
        elif _card_no == 8:
            printing_and_logging(f'Bank pays you dividend of $50')
            player.bank_transaction(50)
        elif _card_no == 9:
            printing_and_logging(f'Get Out of Jail Free')
            player.get_out_of_jail_free_card += 1
        elif _card_no == 10:
            printing_and_logging(f'Go Back 3 Spaces')
            player.move(-3)
            printing_and_logging(f'{player} moved three steps back')
            return player.tile_no
        elif _card_no == 11:
            printing_and_logging(f'Go to Jail. Go directly to Jail, do not pass Go, do not collect $200')
            player.move_to(10, collect_go_cash_flag=False)
        elif _card_no == 12:
            printing_and_logging(f'Make general repairs on all your property. For each house pay$25. For each hotel pay $100')
            execute_chance_12(player)
        elif _card_no == 13:
            printing_and_logging(f'Speeding fine $15')
            player.bank_transaction(-15)
        elif _card_no == 14:
            printing_and_logging(f'Take a trip to Reading Railroad. If you pass Go, collect $200')
            player.move_to(reading_railroad.tile_no, collect_go_cash_flag=True)
            return True
        elif _card_no == 15:
            printing_and_logging(f'You have been elected Chairman of the Board. Pay each player $50')
            execute_chance_15(player, kwargs['all_players_list'])
        elif _card_no == 16:
            printing_and_logging(f'Your building loan matures. Collect $150')
            player.bank_transaction(150)


def execute_chance_12(player):
    """
    Execute chance card number 12. Make general repairs on all your property. For each house pay$25. For each hotel pay $100.
    :param player: Player that picked the chance card 12
    :return: The total cost of repairs
    """
    houses = 0
    hotels = 0
    for each_property in player.player_portfolio:
        if type(each_property) == Property:
            houses += each_property._houses
            if each_property._hotel:
                hotels += 1
    repairs_cost = (25 * houses) + (100 * hotels)
    player.bank_transaction(-repairs_cost)

def execute_chance_15(player, players):
    """
    Execute chance card number 15. You have been elected Chairman of the Board. Pay each player $50.
    :param player: The player that picks chance card 15
    :param players: The players being paid the amount.
    """
    other_players = players.copy()
    other_players.remove(player)
    for each_player in other_players:
        player.player_transaction(each_player, -50)

def get_nearest_railroad(player):
    """
    Get the nearest railroad to the player based on which Chance tile they are in.
    :param player: The player that picks chance card 5.
    :return: The railroad tile nearest to the player.
    """
    if player.tile_no == 7:
        nearest_railroad = railroad_properties_list[5]
    if player.tile_no == 22:
        nearest_railroad = railroad_properties_list[25]
    if player.tile_no == 36:
        nearest_railroad = railroad_properties_list[35]
    return nearest_railroad

def execute_chance_5(player):
    """
    Execute chance card no 5. Move the player to the nearest railroad. If the railroad is not owned, buy the property.
    If the railroad is owned by someone, pay twice the rent to them.
    :param player: The player who landed on Chance and picked chance card no 5.
    """
    nearest_railroad = get_nearest_railroad(player)
    player.move_to(nearest_railroad.tile_no, collect_go_cash_flag=False)
    try:
        check_can_buy_asset(player, nearest_railroad)
    except InsufficientFundsError:
        pass
    except PropertyNotFreeError as e:
        landlord = nearest_railroad.owner
        player.pay_rent(landlord, nearest_railroad.rent * 2)
        raise PropertyNotFreeError(nearest_railroad)

def get_nearest_utility(player):
    """
    Get the nearest utility to the player based on which Chance tile they are in.
    :param player: The player that picks chance card 5.
    :return: The utility tile nearest to the player.
    """
    if player.tile_no == 7:
        nearest_utility = utilities_list[12]
    if player.tile_no == 22:
        nearest_utility = utilities_list[28]
    if player.tile_no == 36:
        nearest_utility = utilities_list[28]
    return nearest_utility

def execute_chance_7(player, throw):
    """
    Execute chance card no 7. Move the player to the nearest utility. If the utility is not owned, buy the property.
    If the utility is owned by someone, pay twice the rent to them.
    :param throw: Throw that landed the player in Chance
    :param player: The player who landed on Chance and picked chance card no 5.
    """
    nearest_utility = get_nearest_utility(player)
    player.move_to(nearest_utility.tile_no, collect_go_cash_flag=False)
    try:
        check_can_buy_asset(player, nearest_utility)
    except InsufficientFundsError:
        pass
    except PropertyNotFreeError as e:
        landlord = nearest_utility.owner
        player.pay_rent(landlord, nearest_utility.rent * 2)
        raise PropertyNotFreeError(nearest_utility)