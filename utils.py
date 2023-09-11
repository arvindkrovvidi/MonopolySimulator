from Player import Player


def calculate_networth(player):
    nw = 0
    for asset in player.player_portfolio:
        nw += asset.cost
    nw += player.cash
    return nw


def find_winner(players):
    nw_list = [player.networth for player in players]
    max_nw = max(nw_list)
    winner_index = nw_list.index(max_nw)
    winner = players[winner_index]
    return winner, winner_index


def display_positions(players):
    j = 0
    for i in range(len(players)):
        winner, winner_index = find_winner(players)
        if i != 0:
            if prev.networth == winner.networth:
                yield i - j, winner, winner.networth
                j += 1
                prev = winner
            else:
                yield i + 1, winner, winner.networth
                prev = winner
                j -= 1
                if j < 0:
                    j = 0
        else:
            yield i + 1, winner, winner.networth
            prev = winner
        players.pop(winner_index)
