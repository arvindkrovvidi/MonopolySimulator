from prettytable import PrettyTable

from Player_data import all_players_list as players
from Tiles_data.all_tiles_data import all_tiles_list
from errors import PlayerBrokeError
from player_turn import play_turn
from utils import check_any_player_broke, print_player_summary, printing_and_logging, get_display_options

# TODO: Take all inputs for the program from a file
total_turns = 1000
turn = 1

# TODO: Automate adding players to the all_players_list

game_details = PrettyTable()
game_details.field_names = ["Turn", "Player", "Dice throw", "Current Property", "Cash"]
player_broke = False
while turn <= total_turns or not check_any_player_broke(players):
    for player in players:
        printing_and_logging(f'{player} turn. Location: {all_tiles_list[player.tile_no]}  Cash: {player.cash}')
        if not player.in_jail:
            throw = player.throw_dice()
            player.move(throw)
            current_tile = all_tiles_list[player.tile_no]
            printing_and_logging(f'{player} landed on {current_tile}.')
        else:
            current_tile = all_tiles_list[player.tile_no]
            printing_and_logging(f'{player} is in Jail')
            # TODO: This throw should show two dice individually
            available_options = current_tile.get_available_options(player)
            print(get_display_options(available_options))
            player_option = int(input(f'Select an option from the above: '))
            if current_tile.execute(player, player_option):
                throw = player.throw_dice()
                play_turn(player, player.current_tile, throw=None)
            else:
                break
        try:
            play_turn(player, current_tile, throw)
            printing_and_logging(f"Turn: {turn}, Player: {str(player)}, cash: {player.cash} ")
        except PlayerBrokeError:
            printing_and_logging(f'turn: {turn}, player: {player}, cash: {player.cash}')
            player_broke = True
            print_player_summary(players)
            break
        else:
            game_details.add_row([turn, player.name, throw, current_tile, player.cash])
            printing_and_logging('---------------------------------------------------------------')
    if player_broke:
        break
    turn += 1
    printing_and_logging('=================================================================')

#TODO Add trading properties
#TODO Location of player not updating
#TODO Chance tile moving player to location but not giving option to buy property
#TODO Add mortgaging
#TODO Game hanging after last double throw try
#TODO Display Properties in color in terminal
#TODO Check if you can pay fine and move in the same turn
#TODO Go cash should be paid before options are shown
#TODO View player portfolio during game
#TODO: Display community chest/chance cards information in game
