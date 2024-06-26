from Tiles.Property import Property
from Tiles.Railroad import Railroad
from Tiles.Utility import Utility
from Tiles_data.all_tiles_data import all_tiles_list
from config import printing_and_logging
from errors import PlayerBrokeError
from player_turn import play_turn_jail, throw_move_and_play_turn
from utils import print_player_summary


def main(players, total_turns=1000):
    for each in all_tiles_list:
        if type(each) == Property:
            each._owner = None
            each._houses = 0
            each._hotel = False
            each._mortgaged = False
        elif type(each) in [Railroad, Utility]:
            each._owner = None
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


