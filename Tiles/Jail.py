from Tiles.SpecialTiles import SpecialTiles
from Tiles.Tile import Tile

class Jail(SpecialTiles):
    def __init__(self, tile_no, name, description=None):
        self._description = description
        Tile.__init__(self, tile_no, name)

    def execute(self, player, option):
        if option == 0:
            player.pay_jail_fine()
        elif option == 1:
            player.try_jail_double_throw()
        elif option is not None and option == 2:
            player.get_out_of_jail_free()

    def get_available_options(self, player):
        available_options = ['Pay fine', 'Try double throw']
        if player.get_out_of_jail_free_card:
            available_options.append('Use get out of jail free card')
        return available_options