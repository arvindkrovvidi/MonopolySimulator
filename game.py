from random import randint

from prettytable import PrettyTable

from ChanceTile import ChanceTile
from CommunityChestTile import CommunityChestTile
from Player_data import all_players_list
from Property import Property
from Property_data import properties_list
from Railroad import Railroad
from Utility import Utility
from chance_tiles_data import chance_tiles_list
from community_chest_tiles_data import community_chest_tiles_list
from railroad_property_data import railroad_properties_list
from special_tiles_data import special_tiles_list
from utilities_data import utilities_list
from utils import get_positions, calculate_networth, check_player_has_color_set

# TODO: Take all inputs for the program from a file
total_turns = 100
turn = 0

all_tiles_list = properties_list + special_tiles_list + community_chest_tiles_list + chance_tiles_list + railroad_properties_list + utilities_list

# TODO: Automate adding players to the all_players_list

players = all_players_list

game_details = PrettyTable()
game_details.field_names = ["Turn", "Player", "Dice throw", "Current Property", "Cash"]
while turn <= total_turns:
    for player in players:
        throw = player.throw_dice()
        player.move(throw)
        current_tile = properties_list[player.tile_no]
        if type(current_tile) == Property:
            if current_tile.owner is None:
                player.buy_property(current_tile)
            elif current_tile in player.player_portfolio and check_player_has_color_set(player, current_tile.color):
                player.build_house(current_tile)
            else:
                landlord = current_tile.owner
                player.pay_rent(landlord, current_tile.rent)
        elif type(current_tile) == Railroad:
            if current_tile.owner is None:
                player.buy_property(current_tile)
            else:
                landlord = current_tile.owner
                player.pay_rent(landlord, current_tile.rent)
        elif type(current_tile) == Utility:
            if current_tile.owner is None:
                player.buy_property(current_tile)
            else:
                landlord = current_tile.owner
                if electric_company in landlord.player_portfolio and water_works in landlord.player_portfolio:
                    player.pay_rent(landlord, throw * 10)
                else:
                    player.pay_rent(landlord, throw * 4)
        elif type(current_tile) == CommunityChestTile:
            card_no = randint(1, 16)
            CommunityChestTile.execute(player, card_no)
        elif type(current_tile) == ChanceTile:
            card_no = randint(1,16)
            ChanceTile.execute(player, card_no)
        game_details.add_row([turn, player.name, throw, current_tile, player.cash])
        # TODO: Game did not stop after one player's cash went negative. Check rules to see what happens when player is unable to pay rent.
        if player.cash < 0:
            break
    turn += 1
print(game_details)

for player in players:
    player.networth = calculate_networth(player)

display_winners = PrettyTable()
display_winners.field_names = ["Position", "Player", "Net Worth"]
for pos, win, nw in get_positions(players):
    display_winners.add_row((pos, str(win), nw))
print(display_winners)
# TODO: Add community chests
# TODO: Add chance
# TODO: Add corner tiles
# TODO: Add progress bar
# TODO: Run a profiler to check for possible optimizations
# TODO: Add tests for all functions
# TODO: Check for code coverage
# TODO: Push code to GIT
# TODO: Add hotels and houses
# TODO Add descriptions for functions
# TODO: Automatically create test functions and give suggestions to create test functions when a function is selected.
# TODO: Calculate probabilities for each person winning the game
