from random import randint

from prettytable import PrettyTable

from ChanceTile import ChanceTile
from CommunityChestTile import CommunityChestTile
from Player import Player
from Property import Property
from Property_data import all_properties_list, property_tracker
from chance_tiles_data import chance_tiles_list
from community_chest_tiles_data import community_chest_tiles_list
from special_tiles_data import special_tiles_list
from utils import display_positions, calculate_networth

# TODO: Take all inputs for the program from a file
total_turns = 100
turn = 0

all_tiles_list = all_properties_list + special_tiles_list + community_chest_tiles_list + chance_tiles_list

# TODO: Automate adding players to the all_players_list
all_players_list = []
arvind = Player("Arvind", 200)
arun = Player("Arun", 200)
adityam = Player("Adityam", 200)
padma = Player("Padma", 200)

all_players_list.append(arvind)
all_players_list.append(arun)
all_players_list.append(adityam)
all_players_list.append(padma)

players = all_players_list

game_details = PrettyTable()
game_details.field_names = ["Turn", "Player", "Dice throw", "Current Property", "Cash"]
while turn <= total_turns:
    for player in players:
        throw = player.throw_dice()
        player.move(throw)
        current_tile = all_properties_list[player.tile_no]
        if type(current_tile) == Property:
            if current_tile not in property_tracker:
                player.buy_property(current_tile)
            else:
                landlord = property_tracker[current_tile]
                player.pay_rent(landlord, current_tile.rent)
        else:
            if type(current_tile) == CommunityChestTile:
                # TODO: Implement what to do when player lands on Community chest tile
                pass
            if type(current_tile) == ChanceTile:
                # TODO: Change 5 to 16 after implementing all chance cards
                card_no = randint(1,5)
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
for pos, win, nw in display_positions(players):
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
# TODO: Add hotels
# TODO Add descriptions for functions
