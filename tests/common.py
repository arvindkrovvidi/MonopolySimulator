def buy_color_set(player, asset_1, asset_2, asset_3):
    for asset in [asset_1, asset_2, asset_3]:
        player.buy_asset(asset)
def build_houses(player, asset_1, asset_2, asset_3, num_houses):
    buy_color_set(player, asset_1, asset_2, asset_3)
    for i in range(0,num_houses):
        for asset in [asset_1, asset_2, asset_3]:
            player.build_house(asset)

def build_all_hotels(player, asset_1, asset_2, asset_3):
    build_houses(player, asset_1, asset_2, asset_3, 4)
    for asset in [asset_1, asset_2, asset_3]:
        player.build_hotel(asset)