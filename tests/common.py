def buy_color_set(player, assets):
    for asset in assets:
        player.buy_asset(asset)
def build_houses(player, assets, num_houses):
    buy_color_set(player, assets)
    for i in range(0,num_houses):
        for asset in assets:
            player.build_house(asset)

def build_all_hotels(player, assets):
    build_houses(player, assets, 4)
    for asset in assets:
        player.build_hotel(asset)