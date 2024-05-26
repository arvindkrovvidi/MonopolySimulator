import pytest

from tests.common import buy_assets
from turn_based_game import main


# def test_main_1(mocker, arvind, arun, st_charles_place):
#     """
#     Test main function when one of the players goes broke
#     """
#     arvind.cash = 0
#     arun.cash = 0
#     mocker.patch.object(arun, 'throw_dice', side_effect=[11, 9])
#     mocker.patch('player_turn.get_player_input', side_effect=[2, 0, 2])
#     mocker.patch.object(arvind, 'throw_dice', side_effect=[5, 6])
#     mocker.patch('player_turn.get_player_input', return_value=0)
#     players = [arun, arvind]
#     main(players, total_turns=10)
#
#     assert players == [arun]

def test_main_2(mocker, arvind, arun):
    """
    Test main when player lands on Chance 22, picks chance card 5, moves to B&O railroad that is already owned by another player
    """
    all_players_list = [arun, arvind]
    mocker.patch.object(arun, 'throw_dice', side_effect=[10, 10, 5])
    mocker.patch.object(arvind, 'throw_dice', side_effect=[10, 10, 2])
    mocker.patch('player_turn.get_player_input', side_effect=[0, 0, 0, 0, 2, 0, 0])
    mocker.patch('player_turn.randint', return_value=5)
    main(players=all_players_list, total_turns=3)

    assert arvind.cash == 350
    assert arun.cash == 250
    assert arvind.tile_no == 25

@pytest.mark.skip(reason="properties inside all_tiles_list not getting reset after previous test.")
def test_main_3(mocker, arvind, arun):
    """
    Test main when player lands on Chance 22, picks chance card 5, moves to B&O railroad that is not owned by another player
    """
    all_players_list = [arun, arvind]
    mocker.patch.object(arun, 'throw_dice', side_effect=[10, 10, 5])
    mocker.patch('player_turn.get_player_input', side_effect=[1, 0, 0])
    mocker.patch.object(arvind, 'throw_dice', side_effect=[10, 10, 2])
    mocker.patch('player_turn.randint', return_value=5)
    main(players=all_players_list, total_turns=3)

    assert arvind.cash == 200
    assert arun.cash == 400
    assert arvind.tile_no == 25

# def test_main_4(mocker, arvind, states_avenue, st_charles_place, virginia_avenue):
#     """
#     Test main when player lands in jail but should have the option to build houses
#     """
#     arvind.cash = 1500
#     mocker.patch.object(arvind, 'throw_dice', return_value=10)
#     arvind.throw_dice()
#     arvind.throw_dice()
#     arvind.throw_dice()
#     buy_assets(arvind, [states_avenue, st_charles_place, virginia_avenue])
#     mocker.patch('player_turn.get_player_input', side_effect=[0, 0, 0, 1])
#     main([arvind], total_turns=5)

    assert states_avenue._houses == 1

def test_main_5(mocker, arvind, arun):
    """
    Test double throws when two players are in jail
    """
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4])
    mocker.patch.object(arun, 'throw_one_dice', side_effect=[6, 4, 6, 4, 6, 4, 6, 4, 6, 4, 6, 4])
    mocker.patch('player_turn.get_player_input', side_effect=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0])
    main([arvind, arun], total_turns=6)

def test_main_6(mocker, arvind, arun):
    """
    Test double throws when two players land in jail from community chest
    """
    mocker.patch.object(arvind, 'throw_dice', return_value=2)
    mocker.patch.object(arun, 'throw_dice', return_value=2)
    mocker.patch('player_turn.randint', return_value=6)
    mocker.patch('player_turn.get_player_input', side_effect=[0, 0, 1, 1, 1, 1, 1, 0, 1, 0])
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[1, 2, 1, 2, 1, 2])
    mocker.patch.object(arun, 'throw_one_dice', side_effect=[1, 2, 1, 2, 1, 2])
    main([arvind, arun], total_turns=4)

    assert arvind.cash == 350
    assert arun.cash == 350
    assert arvind.tile_no == 13
    assert arun.tile_no == 13
def test_main_7(mocker, arvind, arun):
    """
    Test double throws when two players land in jail from chance
    """
    mocker.patch.object(arvind, 'throw_dice', return_value=2)
    mocker.patch.object(arun, 'throw_dice', return_value=2)
    mocker.patch('player_turn.randint', return_value=6)
    mocker.patch('player_turn.get_player_input', side_effect=[0, 0, 1, 1, 1, 1, 1, 0, 1, 0])
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[1, 2, 1, 2, 1, 2])
    mocker.patch.object(arun, 'throw_one_dice', side_effect=[1, 2, 1, 2, 1, 2])
    main([arvind, arun], total_turns=4)

    assert arvind.cash == 350
    assert arvind.cash == 350
    assert arvind.tile_no == 13
    assert arun.tile_no == 13

def test_main_8(mocker, arvind, states_avenue, st_charles_place, virginia_avenue):
    """
    Test play_turn when player lands on chance tile and should have the option to build house
    """
    arvind.cash = 1500
    buy_assets(arvind, [states_avenue, st_charles_place, virginia_avenue])
    mocker.patch.object(arvind, 'throw_dice', return_value=7)
    mocker.patch('player_turn.randint', return_value=8)
    mocker.patch('player_turn.get_player_input', side_effect=[2, 0, 0])
    main([arvind], total_turns=1)

    assert states_avenue._houses == 1
    assert arvind.cash == 1210

def test_main_9(mocker, arvind, states_avenue, st_charles_place, virginia_avenue):
    """
    Test main when player lands on community chest tile and should have the option to build house
    """
    arvind.cash = 1500
    buy_assets(arvind, [states_avenue, st_charles_place, virginia_avenue])
    mocker.patch.object(arvind, 'throw_dice', return_value=2)
    mocker.patch('player_turn.randint', return_value=2)
    mocker.patch('player_turn.get_player_input', side_effect=[2, 0, 0])
    main([arvind], total_turns=1)

    assert states_avenue._houses == 1
    assert arvind.cash == 1360

def test_main_10(mocker, arvind):
    """
    Test main when the player rolls a double on the third try
    """
    arvind.cash = 500
    mocker.patch.object(arvind, 'throw_dice', side_effect=[10, 10, 10])
    mocker.patch('player_turn.get_player_input', side_effect=[0, 0, 0, 1, 1, 1, 0])
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[1, 2, 1, 2, 2, 2])
    main([arvind], total_turns=6)

    assert arvind.cash == 700

def test_main_11(mocker, arvind, arun):
    """
    Test main when player lands on Chance 22, picks chance card 7, moves to Water Works that is already owned by another player
    """
    all_players_list = [arun, arvind]
    mocker.patch.object(arun, 'throw_dice', side_effect=[10, 10, 8])
    mocker.patch.object(arvind, 'throw_dice', side_effect=[10, 10, 2])
    mocker.patch('player_turn.get_player_input', side_effect=[0, 0, 0, 0, 2, 0, 0])
    mocker.patch('player_turn.randint', return_value=7)
    main(players=all_players_list, total_turns=3)

    assert arvind.cash == 384
    assert arun.cash == 266
    assert arvind.tile_no == 28

def test_main_12(mocker, arvind):
    """
    Test main when player lands on Chance 22, picks chance card 7, moves to Water Works that is not owned by another player
    """
    mocker.patch.object(arvind, 'throw_dice', side_effect=[10, 10, 2])
    mocker.patch('player_turn.get_player_input', side_effect=[0, 0, 2, 0])
    mocker.patch('player_turn.randint', return_value=7)
    main(players=[arvind], total_turns=3)

    assert arvind.cash == 250
    assert arvind.tile_no == 28

def test_main_13(mocker, arvind, st_charles_place):
    """
    Test main
    1. Player throws a 2 and lands on Community chest
    2. Player picks card 1
    3. Player moves to go and collects 200 as the card says
    4. Player throws again.
    5. Player throws again, lands in St. Charles place. Player collects 200 for passing go.
    """
    arvind.cash = 1300
    mocker.patch('player_turn.get_player_input', side_effect=[0, 0])
    mocker.patch('player_turn.randint', return_value=1)
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[1, 1, 5, 6])
    main([arvind], total_turns=1)

    assert arvind.cash == 1900
    assert arvind.current_tile == st_charles_place

