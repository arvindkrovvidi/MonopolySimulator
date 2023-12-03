from Tiles_data.all_tiles_data import all_tiles_list
from config import printing_and_logging
from errors import PlayerBrokeError
from player_turn import play_turn_jail, throw_move_and_play_turn
from utils import print_player_summary


def main(players, total_turns=1000, all_tiles_list=all_tiles_list):
    turn = 1
    player_broke = False

    while turn <= total_turns:
        for player in players:
            try:
                printing_and_logging(f'{player} turn. Location: {all_tiles_list[player.tile_no]}  Cash: {player.cash}')
                if not player.in_jail:
                    throw_move_and_play_turn(player)
                    if player.double_counter == 1:
                        throw_move_and_play_turn(player)
                    if player.double_counter == 2:
                        throw_move_and_play_turn(player)
                    if player.double_counter == 3:
                        player.move_to(10, collect_go_cash_flag=False)
                else:
                    play_turn_jail(player)
                printing_and_logging(f'Turn: {turn}    Player: {player}    Location: {all_tiles_list[player.tile_no]}    Cash: {player.cash}')
            except PlayerBrokeError as e:
                printing_and_logging(f'Turn: {turn}    Player: {player}    Location: {all_tiles_list[player.tile_no]}    Cash: {player.cash}')
                players.remove(e.player)
                print_player_summary(players)
                player_broke = True
                break
            else:
                printing_and_logging('---------------------------------------------------------------')
        turn += 1
        printing_and_logging('=================================================================')
        if player_broke:
            break

if __name__ == "__main__":
    from Player_data import all_players_list as players
    main(players)
#TODO Add trading properties
#TODO Add mortgaging
#TODO View player portfolio during game
#TODO Add "purchase get out of jail free card from another player" function
#TODO "No more houses to sell" remove this print statement
#TODO Arvind does not have enough cash to build a house on States Avenue printing twice
#TODO Have one main execute function for all kinds of tiles in the base class. Override this function in the child classes.
#TODO Print messages can be a second return variable from the check functions that can be printed when required.
#TODO Replace all_tiles_list with all_tiles_list fixture in tests
