from player_turn import play_turn_property
def test_play_turn_property_free(arvind, st_james_place):
    """
    Test play_turn_property when player lands on free property
    """
    play_turn_property(st_james_place, arvind)
    assert st_james_place in arvind.player_portfolio
    assert arvind.cash == 20

def test_play_turn_property_bought(arvind, arun, st_james_place):
    """
    Test play_turn_property when the property is already owned by another player
    """
    arun.buy_asset(st_james_place)
    play_turn_property(st_james_place, arvind)
    assert arun.cash == 34
    assert arvind.cash == 186

# def test_play_turn_property_color_set_true(arvind, st_charles_place, states_avenue, virginia_avenue):
#     arvind.cash = 1000
#     arvind.buy_asset(st_charles_place)
#     arvind.buy_asset(states_avenue)
#     arvind.buy_asset(virginia_avenue)
#     play_turn_property(states_avenue, arvind)
#     assert
