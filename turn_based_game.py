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
                printing_and_logging(f'turn: {turn}, player: {player}, cash: {player.cash}')
                print_player_summary(players)
            else:
                turn += 1
                printing_and_logging('---------------------------------------------------------------')
        printing_and_logging('=================================================================')

if __name__ == "__main__":
    main()
#TODO Add trading properties
#TODO Add mortgaging
#TODO View player portfolio during game
#TODO Add "purchase get out of jail free card from another player" function
#TODO Add ability to keep playing until the player selects end turn option
#TODO Player need not land on a property to build houses/hotels on it.
#TODO If player does not roll a double in third turn, they pay 50 and get out of jail and move to the tile with that third throw. Player should be able to play their turn after landing ona tile.
#TODO If player pays fine, they can get out in the same turn and be able to play that turn.
#TODO "No more houses to sell" remove this print statement
#TODO When Arvind lands in jail and chooses to try double throw, he gets his 3 chances immediately without other players getting their chances in the middle
#TODO Arvind does not have enough cash to build a house on States Avenue printing twice
#TODO Player not getting second turn for throwing double when the first turn of the double gave only 1 option(end turn)
#TODO Player that goes bankrupt loses immediately. The other players calculate their networths. The one with highest networth wins the game.
#TODO Player should not be able to play the turn and instead go to jail on the third double.
#TODO Set double counter to 0 after player lands in jail. Player does not get to play again when they throw a double to get out of jail(using any of the three methods)
#TODO Build hotel option appearing without player building 4 houses on all properties in the color set
#TODO Handle invalid inputs