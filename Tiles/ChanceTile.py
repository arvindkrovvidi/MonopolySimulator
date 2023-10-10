from Player_data import all_players_list
from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile
from Tiles_data.Property_data import boardwalk, illinois_avenue, st_charles_place
from Tiles_data.railroad_property_data import reading_railroad, railroad_properties_list
from Tiles_data.special_tiles_data import go
from Tiles_data.utilities_data import utilities_list
from utils import check_passing_go, check_player_has_color_set


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
        if _card_no == 1:
            player.move_to(boardwalk.tile_no, collect_go_cash_flag=False)
        elif _card_no == 2:
            player.move_to(go.tile_no, collect_go_cash_flag=False)
        elif _card_no == 3:
            player.move_to(illinois_avenue.tile_no, collect_go_cash_flag=check_passing_go(player, illinois_avenue))
        elif _card_no == 4:
            player.move_to(st_charles_place.tile_no, collect_go_cash_flag=check_passing_go(player, illinois_avenue))
        elif _card_no == 5:
            execute_chance_5(player)
        elif _card_no == 6:
            execute_chance_5(player)
        elif _card_no == 7:
            execute_chance_7(player, kwargs['throw'])
        elif _card_no == 8:
            player.bank_transaction(50)
        elif _card_no == 9:
            player.get_out_of_jail_free_card += 1
        elif _card_no == 10:
            pass
        elif _card_no == 11:
            player.move_to(10, collect_go_cash_flag=False)
        elif _card_no == 12:
            execute_chance_12(player)
        elif _card_no == 13:
            player.bank_transaction(-15)
        elif _card_no == 14:
            player.move_to(reading_railroad.tile_no, collect_go_cash_flag=True)
        elif _card_no == 15:
            execute_chance_15(player, all_players_list)
        elif _card_no == 16:
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
    if nearest_railroad.owner is None:
        player.buy_railroad(nearest_railroad)
    elif nearest_railroad not in player.player_portfolio:
        landlord = nearest_railroad.owner
        player.pay_rent(landlord, nearest_railroad.rent[landlord.railroads_owned - 1] * 2)

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
    Execute chance card no 5. Move the player to the nearest utility. If the utility is not owned, buy the property.
    If the utility is owned by someone, pay twice the rent to them.
    :param throw: Throw that landed the player in Chance
    :param player: The player who landed on Chance and picked chance card no 5.
    :param tracker: The property tracker that tracks properties and their owners.
    """
    nearest_utility = get_nearest_utility(player)
    player.move_to(nearest_utility.tile_no, collect_go_cash_flag=False)
    if nearest_utility.owner is None:
        player.buy_utility(nearest_utility)
    else:
        landlord = nearest_utility.owner
        if check_player_has_color_set(landlord, "Utility"):
            player.pay_rent(landlord, throw * 10)
        else:
            player.pay_rent(landlord, throw * 4)