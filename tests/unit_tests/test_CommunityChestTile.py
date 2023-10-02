from CommunityChestTile import execute_chest_9
def test_execute_chest_9(arvind_fx, arun_fx, adityam_fx, padma_fx):
    all_players = [arvind_fx, arun_fx, adityam_fx, padma_fx]
    execute_chest_9(arvind_fx, all_players)
    assert arvind_fx.cash == 230
    assert arun_fx.cash == 190
    assert adityam_fx.cash == 190
    assert padma_fx.cash == 190