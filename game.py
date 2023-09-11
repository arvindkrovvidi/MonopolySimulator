from Player import Player
from Tile import all_properties_list
from Property_data import property_tracker
from utils import calculate_networth, find_winner
from prettytable import PrettyTable

total_turns = 100
turn = 0

# TODO: Automate adding players to the all_players_list
all_players_list = []
arvind = Player("Arvind", 200)
arun = Player("Arun", 200)
adityam = Player("Adityam", 200)
padma = Player("Padma", 200)
all_players_list.append(arvind)
all_players_list.append(arun)
all_players_list.append(adityam)
all_players_list.append(padma)
players = all_players_list

while turn <= total_turns:
    for player in players:
        throw = player.throw_dice()
        player.move(throw)
        current_property = all_properties_list[player.tile_no]
        if current_property not in property_tracker:
            player.buy_property(current_property)
        else:
            landlord = property_tracker[current_property]
            player.pay_rent(landlord, current_property.rent)
        # TODO: Improve display of below details.
        game_details = PrettyTable()
        game_details.field_names = ["Turn", "Player", "Dice throw", "Current Property", "Cash"]
        game_details.add_row([turn, player.name, throw, current_property, player.cash])
        print(game_details)
        if player.cash < 0:
            break
    turn += 1
# TODO: improve display of details below
# TODO: generalize below printing for multiple players
for player in players:
    print(f"{player} cash: {player.cash}")
    player.networth = calculate_networth(player)
    print(f'{player.name} NW: {player.networth} ')


winner = find_winner(players)
print(f'{winner} wins!')

# TODO: Add community chests
# TODO: Add chance
# TODO: Add corner tiles
# TODO: Add progress bar
# TODO: Run a profiler to check for possible optimizations
# TODO: Add tests for all functions
# TODO: Check for code coverage
# TODO: Push code to GIT
