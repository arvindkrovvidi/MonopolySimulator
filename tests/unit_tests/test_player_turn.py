# from player_turn import play_turn_property
#
# def buy_property(arvind, st_james_place):
#     st_james_place.owner = arvind
#     arvind.cash = 20
#     arvind.player_portfolio.append(st_james_place)
# def test_play_turn_property_free_no_color_set(mocker, arvind, st_james_place):
#     mocker.patch('player_turn.buy_property', side_effect=buy_property)
#     play_turn_property(st_james_place, arvind)
#     assert st_james_place in arvind.player_portfolio
