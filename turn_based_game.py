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
                    player.move(throw)
                    current_tile = all_tiles_list[player.tile_no]
                    play_turn(player, current_tile, throw)
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
#TODO View player portfolio during game
#TODO Add "purchase get out of jail free card from another player" function
#TODO Add ability to keep playing until the player selects end turn option
#TODO Player need not land on a property to build houses/hotels on it.
#TODO If player does not roll a double in third turn, they pay 50 and get out of jail and move to the tile with that third throw. Player should be able to play their turn after landing ona tile.
#TODO If player pays fine, they can get out in the same turn and be able to play that turn.
#TODO "No more houses to sell" remove this print statement
#TODO When Arvind lands in jail and chooses to try double throw, he gets his 3 chances immediately without other players getting their chances in the middle
#TODO Arvind does not have enough cash to build a house on States Avenue printing twice
#TODO It is your birthday. Collect $10 from every player. Collecting from self.
#TODO After passing go, display cash
#TODO Player not getting second turn for throwing double when the first turn of the double gave only 1 option(end turn)
#TODO Player that goes bankrupt loses immediately. The other players calculate their networths. The one with highest networth wins the game.