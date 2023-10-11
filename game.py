from prettytable import PrettyTable

from Player_data import all_players_list
from Tiles_data.Property_data import properties_list
from Tiles_data.chance_tiles_data import chance_tiles_list
from Tiles_data.community_chest_tiles_data import community_chest_tiles_list
from Tiles_data.railroad_property_data import railroad_properties_list
from Tiles_data.special_tiles_data import special_tiles_list
from Tiles_data.utilities_data import utilities_list
from errors import PlayerBrokeError, PropertyNotFreeError
from player_turn import play_turn
from utils import check_any_player_broke, print_player_summary

# TODO: Take all inputs for the program from a file
total_turns = 1000
turn = 0

all_tiles_list = properties_list + special_tiles_list + community_chest_tiles_list + chance_tiles_list + railroad_properties_list + utilities_list

# TODO: Automate adding players to the all_players_list

players = all_players_list

game_details = PrettyTable()
game_details.field_names = ["Turn", "Player", "Dice throw", "Current Property", "Cash"]
player_broke = False
while turn <= total_turns or not check_any_player_broke(all_players_list):
    for player in players:
        throw = player.throw_dice()
        player.move(throw)
        current_tile = properties_list[player.tile_no]
        try:
            play_turn(current_tile, player, throw)
        except PlayerBrokeError:
            print(f'turn: {turn}, player: {player}, cash: {player.cash}')
            player_broke = True
            print_player_summary(players)
            break
        except PropertyNotFreeError:
            raise SystemExit
        else:
            game_details.add_row([turn, player.name, throw, current_tile, player.cash])
            turn += 1
    if player_broke:
        break
# print(game_details)



# TODO: Add chance
# TODO: Add progress bar
# TODO: Run a profiler to check for possible optimizations
# TODO: Add tests for all functions
# TODO: Check for code coverage
# TODO: Push code to GIT
# TODO: Calculate probabilities for each person winning the game
# TODO: Add exceptions