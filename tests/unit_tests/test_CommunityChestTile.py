from CommunityChestTile import execute_chest_9
def test_execute_chest_9(arvind, arun, adityam, padma):
    all_players = [arvind, arun, adityam, padma]
    execute_chest_9(arvind, all_players)
    assert arvind.cash == 230
    assert arun.cash == 190
    assert adityam.cash == 190
    assert padma.cash == 190