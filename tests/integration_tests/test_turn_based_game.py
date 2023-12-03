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

def test_main_2(mocker, arvind, arun):
    """
    Test main when player lands on Chance 22, picks chance card 5, moves to B&O railroad that is already owned by another player
    """
    all_players_list = [arun, arvind]
    mocker.patch.object(arun, 'throw_dice', side_effect=[10, 10, 5])
    mocker.patch('player_turn.get_player_input', return_value=0)
    mocker.patch.object(arvind, 'throw_dice', side_effect=[10, 10, 5])
    mocker.patch('player_turn.get_player_input', return_value=0)
    main(players=all_players_list, total_turns=3)

    assert arvind.cash == 375
    assert arun.cash == 225
    assert arvind.tile_no == 25