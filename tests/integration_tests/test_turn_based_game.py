import pytest

from tests.common import buy_assets
from turn_based_game import main


def test_main_1(mocker, arvind, arun, st_charles_place):
    """
    Test main function when one of the players goes broke
    """
    arvind.cash = 0
    mocker.patch.object(arun, 'throw_dice', side_effect=[11, 9])
    mocker.patch('player_turn.get_player_input', return_value=0)
    mocker.patch.object(arvind, 'throw_dice', side_effect=[5, 6])
    mocker.patch('player_turn.get_player_input', return_value=0)
    players = [arun, arvind]
    main(players, total_turns=10)

    assert players == [arun]

def test_main_2(mocker, arvind, arun, all_tiles_list):
    """
    Test main when player lands on Chance 22, picks chance card 5, moves to B&O railroad that is already owned by another player
    """
    all_players_list = [arun, arvind]
    mocker.patch.object(arun, 'throw_dice', side_effect=[10, 10, 5])
    mocker.patch('player_turn.get_player_input', return_value=0)
    mocker.patch.object(arvind, 'throw_dice', side_effect=[10, 10, 2])
    mocker.patch('player_turn.get_player_input', return_value=0)
    mocker.patch('player_turn.randint', return_value=5)
    main(players=all_players_list, total_turns=3, all_tiles_list=all_tiles_list)

    assert arvind.cash == 350
    assert arun.cash == 250
    assert arvind.tile_no == 25

@pytest.mark.skip(reason="properties inside all_tiles_list not getting reset after previous test.")
def test_main_3(mocker, arvind, arun, all_tiles_list):
    """
    Test main when player lands on Chance 22, picks chance card 5, moves to B&O railroad that is not owned by another player
    """
    all_players_list = [arun, arvind]
    mocker.patch.object(arun, 'throw_dice', side_effect=[10, 10, 5])
    mocker.patch('player_turn.get_player_input', side_effect=[1, 0, 0])
    mocker.patch.object(arvind, 'throw_dice', side_effect=[10, 10, 2])
    mocker.patch('player_turn.randint', return_value=5)
    main(players=all_players_list, total_turns=3, all_tiles_list=all_tiles_list)

    assert arvind.cash == 200
    assert arun.cash == 400
    assert arvind.tile_no == 25

def test_main_4(mocker, arvind, states_avenue, st_charles_place, virginia_avenue, all_tiles_list):
    """
    Test main when player lands in jail but should have the option to build houses
    """
    arvind.cash = 1500
    mocker.patch.object(arvind, 'throw_dice', return_value=10)
    arvind.throw_dice()
    arvind.throw_dice()
    arvind.throw_dice()
    buy_assets(arvind, [states_avenue, st_charles_place, virginia_avenue])
    mocker.patch('player_turn.get_player_input', side_effect=[1, 1, 0, 0, 2, 0, 2])
    main([arvind], all_tiles_list=all_tiles_list, total_turns=4)

    assert states_avenue._houses == 1
