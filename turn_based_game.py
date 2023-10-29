from prettytable import PrettyTable

from Player_data import all_players_list as players
from Tiles_data.all_tiles_data import all_tiles_list
from config import logger
from errors import PlayerBrokeError
from player_turn import get_available_options_properties, run_player_option
from utils import check_any_player_broke, print_player_summary, get_display_options

# TODO: Take all inputs for the program from a file
total_turns = 1000
turn = 1

# TODO: Automate adding players to the all_players_list

game_details = PrettyTable()
game_details.field_names = ["Turn", "Player", "Dice throw", "Current Property", "Cash"]
player_broke = False
while turn <= total_turns or not check_any_player_broke(players):
    for player in players:
        print(f'{player} turn')
        throw = player.throw_dice()
        player.move(throw)
        current_tile = all_tiles_list[player.tile_no]
        print(f'{player} landed on {current_tile}')
        logger.info(f'{player} landed on {current_tile}')
        try:
            available_options = get_available_options_properties(current_tile, player, throw)
            if available_options is not None:
                option_function_dict = dict(list(enumerate(available_options)))
                print(get_display_options(available_options))
                user_input = int(input('Select an option from the above: '))
                run_player_option(player, current_tile, option_function_dict, user_input)
            print(f"Turn: {turn}, Player: {str(player)}, cash: {player.cash} ")
            logger.info(f"Turn: {turn}, Player: {str(player)}, cash: {player.cash} ")
        except PlayerBrokeError:
            print(f'turn: {turn}, player: {player}, cash: {player.cash}')
            player_broke = True
            print_player_summary(players)
            break
        else:
            game_details.add_row([turn, player.name, throw, current_tile, player.cash])
            logger.info('---------------------------------------------------------------')
    if player_broke:
        break
    turn += 1
    logger.info('=================================================================')

# TODO: combine print and log into one function