from Tiles_data.all_tiles_data import all_tiles_list
def test_execute_option_0(arvind, jail):
    """
    Test execute when player selects pay_jail_fine
    """
    arvind.move_to(10, collect_go_cash_flag=False)
    current_tile = all_tiles_list[arvind.tile_no]
    current_tile.execute(arvind, 0)

    assert arvind.cash == 150

def test_execute_option_1(mocker, arvind, jail):
    """
    Test execute when player selects try_jail_double_throw and throws a double.
    """
    arvind.move_to(10, collect_go_cash_flag=False)
    assert arvind.in_jail == True
    current_tile = all_tiles_list[arvind.tile_no]
    mocker.patch.object(arvind, 'throw_one_dice', return_value=5)
    current_tile.execute(arvind, 1)
    assert arvind.in_jail == False

def test_execute_option_2(mocker, arvind, jail):
    """
    Test execute when player selects try_jail_double_throw and throws a double.
    """
    arvind.move_to(10, collect_go_cash_flag=False)
    assert arvind.in_jail == True
    current_tile = all_tiles_list[arvind.tile_no]
    mocker.patch.object(arvind, 'throw_one_dice', side_effect=[5, 4])
    current_tile.execute(arvind, 1)
    assert arvind.in_jail == True

def test_execute_option_3(arvind, chest_2):
    """
    Test execute when player selects get_out_of_jail_free.
    """
    arvind.move_to(2)
    current_tile = all_tiles_list[arvind.tile_no]
    current_tile.execute(arvind, 5)
    assert arvind.get_out_of_jail_free_card == True

    arvind.move_to(10)
    assert arvind.in_jail == True
    current_tile = all_tiles_list[arvind.tile_no]
    current_tile.execute(arvind, 2)
    assert arvind.in_jail == False

def test_get_available_options(arvind):
    """
    Test get_available_options
    """
    arvind.move_to(10)
    assert arvind.in_jail == True
    current_tile = all_tiles_list[arvind.tile_no]
    actual = current_tile.get_available_options(arvind)
    assert actual == ['Pay fine', 'Try double throw']

    arvind.move_to(2)
    current_tile = all_tiles_list[arvind.tile_no]
    current_tile.execute(arvind, 5)
    assert arvind.get_out_of_jail_free_card == True

    arvind.move_to(10)
    assert arvind.in_jail == True
    current_tile = all_tiles_list[arvind.tile_no]
    actual = current_tile.get_available_options(arvind)
    assert actual == ['Pay fine', 'Try double throw', 'Use get out of jail free card']

