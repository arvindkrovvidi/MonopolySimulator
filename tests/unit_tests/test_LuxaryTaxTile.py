from Tiles_data.special_tiles_data import luxury_tax
def test_execute(arvind):
    luxury_tax.execute(arvind)
    assert arvind.cash == 100