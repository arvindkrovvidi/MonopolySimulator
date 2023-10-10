from Tiles.CommunityChestTile import execute_chest_9, execute_chest_14
def test_execute_chest_9(arvind, arun, adityam, padma):
    all_players = [arvind, arun, adityam, padma]
    execute_chest_9(arvind, all_players)
    assert arvind.cash == 230
    assert arun.cash == 190
    assert adityam.cash == 190
    assert padma.cash == 190

def test_execute_chest_14(arvind, states_avenue, virginia_avenue, st_james_place):
    arvind.cash = 500
    arvind.player_portfolio.append(states_avenue)
    arvind.player_portfolio.append(virginia_avenue)
    arvind.player_portfolio.append(st_james_place)
    states_avenue._houses = 2
    virginia_avenue._houses = 2
    st_james_place._hotel = True

    execute_chest_14(arvind)
    assert arvind.cash == 225