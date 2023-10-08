from player_turn import play_turn_property


def buy_assets(assets, arvind):
    for asset in assets:
        asset.owner = arvind
        arvind.cash -= asset.cost
        arvind.player_portfolio.append(asset)
def test_play_turn_property_free_no_color_set(mocker, arvind, st_james_place):
    mocker.patch.object(arvind, 'buy_property', side_effect=buy_assets([st_james_place], arvind))
    play_turn_property(st_james_place, arvind)
    assert st_james_place in arvind.player_portfolio
    assert arvind.cash == 20
    assert st_james_place.owner == arvind

def test_play_turn_property_free_color_set(mocker, arvind, st_charles_place, states_avenue, virginia_avenue):
    """
    Test player_turn_property function if the player has the color set.
    """
    arvind.cash = 1500
    arvind.player_portfolio.append(st_charles_place)
    arvind.player_portfolio.append(states_avenue)
    arvind.player_portfolio.append(virginia_avenue)
    virginia_avenue._color_set = True
    mocker.patch.object(arvind, 'buy_property', side_effect=buy_assets([virginia_avenue], arvind))
    play_turn_property(virginia_avenue, arvind)
    assert states_avenue in arvind.player_portfolio
    assert st_charles_place in arvind.player_portfolio
    assert virginia_avenue in arvind.player_portfolio