from Player import Player


def calculate_networth(player):
    nw = 0
    for asset in player.player_portfolio:
        nw += asset.cost
    nw += player.cash
    return nw


# TODO: Check for draws
# TODO: Declare 1st position to last position
def find_winner(players):
    nw_list = [player.net_worth for player in players]
    max_nw = max(nw_list)
    winner_index = nw_list.index(max_nw)
    winner = players[winner_index]
    nw_list.pop(winner_index)
    return winner
