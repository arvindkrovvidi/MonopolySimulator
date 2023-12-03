from turn_based_game import main
def test_main(mocker, arvind, arun, st_charles_place):
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
