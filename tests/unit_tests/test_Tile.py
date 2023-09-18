from Tile import Tile


def test_tile_init():
    tile1 = Tile(1, "Tile1")
    assert tile1.tile_no == 1
    assert tile1.name == "Tile1"
