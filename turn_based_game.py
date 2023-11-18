from Player_data import all_players_list as players
from Tiles_data.all_tiles_data import all_tiles_list
from config import printing_and_logging
from errors import PlayerBrokeError
from player_turn import play_turn_jail, throw_move_and_play_turn
from utils import check_any_player_broke, print_player_summary


def main():
    turn = 1
    total_turns = 1000
    player_broke = False

    while turn <= total_turns or not check_any_player_broke(players):
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
            except PlayerBrokeError:
                printing_and_logging(f'Turn: {turn}    Player: {player}    Location: {all_tiles_list[player.tile_no]}    Cash: {player.cash}')
                print_player_summary(players)
                player_broke = True
                break
            else:
                turn += 1
                printing_and_logging('---------------------------------------------------------------')
        printing_and_logging('=================================================================')
        if player_broke:
            break

if __name__ == "__main__":
    main()
#TODO Add trading properties
#TODO Add mortgaging
#TODO View player portfolio during game
#TODO Add "purchase get out of jail free card from another player" function
#TODO Add ability to keep playing until the player selects end turn option
#TODO Player need not land on a property to build houses/hotels on it.
#TODO "No more houses to sell" remove this print statement
#TODO Arvind does not have enough cash to build a house on States Avenue printing twice
#TODO Player that goes bankrupt loses immediately. The other players calculate their networths. The one with highest networth wins the game.
#TODO Handle invalid inputs