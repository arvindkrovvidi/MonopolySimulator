from Player_data import all_players_list as players
from Tiles_data.all_tiles_data import all_tiles_list
from config import printing_and_logging
from errors import PlayerBrokeError
from player_turn import play_turn
from utils import check_any_player_broke, print_player_summary, get_display_options


def main():
    turn = 1
    total_turns = 1000
    player_broke = False

    while turn <= total_turns or not check_any_player_broke(players):
        for player in players:
            printing_and_logging(f'{player} turn. Location: {all_tiles_list[player.tile_no]}  Cash: {player.cash}')
            if not player.in_jail:
                throw = player.throw_dice()
                if player.double_counter == 3:
                    player.move_to(10, collect_go_cash_flag=False)
                else:
                    player.move(throw)
                current_tile = all_tiles_list[player.tile_no]
                printing_and_logging(f'{player} landed on {current_tile}.')
            else:
                current_tile = all_tiles_list[player.tile_no]
                printing_and_logging(f'{player} is in Jail')
                available_options = current_tile.get_available_options(player)
                print(get_display_options(available_options))
                player_option = int(input(f'Select an option from the above: '))
                throw = current_tile.execute(player, player_option)
                if throw is not None:
                    play_turn(player, player.current_tile, throw)
                else:
                    break
            try:
                play_turn(player, current_tile, throw)
                printing_and_logging(f"Turn: {turn}, Player: {str(player)}, cash: {player.cash} ")
                if player.double_counter in [1, 2]:
                    throw = player.throw_dice()
                    play_turn(player, current_tile, throw)
                printing_and_logging(f"Turn: {turn}, Player: {str(player)}, cash: {player.cash} ")
            except PlayerBrokeError:
                printing_and_logging(f'turn: {turn}, player: {player}, cash: {player.cash}')
                player_broke = True
                print_player_summary(players)
                break
            else:
                printing_and_logging('---------------------------------------------------------------')
        if player_broke:
            break
        turn += 1
        printing_and_logging('=================================================================')

if __name__ == "__main__":
    main()
#TODO Add trading properties
#TODO Add mortgaging
#TODO Game hanging after last double throw try
#TODO View player portfolio during game
#TODO Add "purchase get out of jail free card from another player" function
#TODO Add ability to keep playing until the player selects end turn option
#TODO Player need not land on a property to build houses/hotels on it.