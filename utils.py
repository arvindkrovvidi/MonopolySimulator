from Player import Player
from Tile import Tile


def calculate_networth(player) -> int:
    """
    Calculate networth of a player
    :param player: Player who's networth is being calculated
    :return: Networth
    """
    nw = 0
    for asset in player.player_portfolio:
        nw += asset.cost
    nw += player.cash
    return nw


def find_winner(players):
    """
    Find the winner of the game based on networths
    :param players: List of all the players in the game
    :return: Winner and their index in the list
    """
    nw_list = [player.networth for player in players]
    max_nw = max(nw_list)
    winner_index = nw_list.index(max_nw)
    winner = players[winner_index]
    return winner, winner_index


def get_positions(players):
    """
    Generator that yields the position, winner and their networth
    :param players: List of all players in the game
    """
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

def check_passing_go(player: Player, tile: Tile) -> bool:
    """
    Check if moving to a tile requires crossing Go tile. This is required for Chance cards.
    :param player: Player that is moving to tile
    :param tile: The tile that the player is moving to.
    :return: True if passing Go else False.
    """
    if player.tile_no < tile.tile_no:
        return False
    else:
        return True