def test_scenario_1(mocker, arvind, jail):
    """
    1. Player lands on jail
    2. Player pays jail fine
    3. Player rolls dice
    4. Player moves to the corresponding tile.
    """
    assert arvind.tile_no == 0
    mocker.patch.object(arvind, 'throw_dice', return_value=10)
    mocker.patch('utils.randint', return_value=1)
    throw = arvind.throw_dice()
    arvind.move(throw)
    assert arvind.tile_no == 10
    current_tile = jail
    current_tile.execute(arvind, 0)
    throw = arvind.throw_dice()
    arvind.move(throw)
    assert arvind.cash == 150
    assert arvind.tile_no == 20

def test_scenario_2(mocker, arvind, jail):
    """
    1. Player lands on jail
    2. Player throws double on the first try
    3. Player rolls dice
    4. Player moves to the corresponding tile.
    """
    assert arvind.tile_no == 0
    mocker.patch.object(arvind, 'throw_dice', return_value=10)
    mocker.patch('utils.randint', return_value=2)
    mocker.patch.object(arvind, 'throw_one_dice', return_value=5)
    throw = arvind.throw_dice()
    arvind.move(throw)
    assert arvind.tile_no == 10
    current_tile = jail
    current_tile.execute(arvind, 1)
    throw = arvind.throw_dice()
    assert arvind.cash == 200
    assert arvind.tile_no == 20

def test_scenario_3(mocker, arvind, jail):
    """
    1. Player lands on jail
    2. Player throws double on the second try
    3. Player rolls dice
    4. Player moves to the corresponding tile.
    """
    assert arvind.tile_no == 0
    mocker.patch.object(arvind, 'throw_dice', return_value=10)
    mocker.patch('utils.randint', return_value=2)
    throw = arvind.throw_dice()
    arvind.move(throw)
    assert arvind.tile_no == 10
    current_tile = jail
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[2, 3])
    current_tile.execute(arvind, 1)
    assert arvind.tile_no == 10
    assert arvind.cash == 200
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[5, 5])
    throw = arvind.throw_dice()
    arvind.move(throw)
    assert arvind.cash == 200
    assert arvind.tile_no == 20
