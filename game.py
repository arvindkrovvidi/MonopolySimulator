from prettytable import PrettyTable

from Player_data import all_players_list
from Property_data import properties_list
from chance_tiles_data import chance_tiles_list
from community_chest_tiles_data import community_chest_tiles_list
from player_turn import play_turn
from railroad_property_data import railroad_properties_list
from special_tiles_data import special_tiles_list
from utilities_data import utilities_list
from utils import get_positions, calculate_networth

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
        play_turn(current_tile, player, throw)
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
