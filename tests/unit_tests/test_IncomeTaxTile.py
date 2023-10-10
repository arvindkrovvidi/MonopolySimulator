from Tiles_data.special_tiles_data import income_tax

def test_execute(arvind):
    income_tax.execute(arvind)
    assert arvind.cash == 0