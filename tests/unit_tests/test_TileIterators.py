from TileIterators import TileDict, TileList


def test_tile_list_get_item(property_list, st_charles_place, states_avenue, virginia_avenue,
                            pennsylvania_railroad):
    assert property_list[11] == st_charles_place
    assert property_list[13] == states_avenue
    assert property_list[14] == virginia_avenue
    assert property_list[15] == pennsylvania_railroad


def test_tile_list_next(property_list, st_charles_place, states_avenue, virginia_avenue,
                        pennsylvania_railroad):
    for asset in property_list:
        print(asset)


def test_tile_list_contains(property_list, st_charles_place, states_avenue, virginia_avenue,
                            pennsylvania_railroad):
    assert states_avenue in property_list
    assert st_charles_place in property_list
    assert pennsylvania_railroad in property_list
    assert virginia_avenue in property_list


def test_tile_list_append(st_charles_place, states_avenue, virginia_avenue,
                          pennsylvania_railroad):
    property_list = TileList([st_charles_place, states_avenue])
    property_list.append(virginia_avenue)
    assert virginia_avenue in property_list
    property_list.append(pennsylvania_railroad)
    assert pennsylvania_railroad in property_list


def test_tile_dict_get_item(property_dict, st_charles_place, states_avenue, virginia_avenue,
                            pennsylvania_railroad, arvind_fx, arun_fx):
    assert property_dict[states_avenue] == arvind_fx
    assert property_dict[st_charles_place] == arun_fx
    assert property_dict[pennsylvania_railroad] == arvind_fx
    assert property_dict[virginia_avenue] == arun_fx


def test_tile_dict_next_item(property_dict, st_charles_place, states_avenue, virginia_avenue,
                             pennsylvania_railroad):
    try:
        while True:
            next(property_dict)
    except StopIteration:
        pass


def test_tile_dict_contains(property_dict, st_charles_place, states_avenue, virginia_avenue,
                            pennsylvania_railroad):
    assert states_avenue in property_dict
    assert st_charles_place in property_dict
    assert pennsylvania_railroad in property_dict
    assert virginia_avenue in property_dict


def test_tile_dict_update(st_charles_place, states_avenue, virginia_avenue,
                          pennsylvania_railroad, arvind_fx, arun_fx):
    property_dict = TileDict({st_charles_place: arvind_fx,
                              states_avenue: arun_fx
                              })
    property_dict.update_dict({pennsylvania_railroad: arvind_fx})
    assert pennsylvania_railroad in property_dict
    assert property_dict[pennsylvania_railroad] == arvind_fx
    property_dict.update_dict({virginia_avenue: arun_fx})
    assert virginia_avenue in property_dict
    assert property_dict[virginia_avenue] == arun_fx


def test_add(arvind_fx, arun_fx, padma_fx, adityam_fx):
    list1 = TileList([arvind_fx, arun_fx])
    list2 = TileList([adityam_fx, padma_fx])
    actual = list1 + list2
    assert type(actual) == TileList
    assert arvind_fx in actual
    assert arun_fx in actual
    assert adityam_fx in actual
    assert padma_fx in actual


def test_keys(arvind_fx, arun_fx, adityam_fx, padma_fx, states_avenue, st_charles_place, pennsylvania_railroad,
              virginia_avenue):
    tile_dict = TileDict({states_avenue: arvind_fx,
                          st_charles_place: arun_fx,
                          pennsylvania_railroad: adityam_fx,
                          virginia_avenue: padma_fx})
    keys = tile_dict.keys()
    assert states_avenue in keys
    assert st_charles_place in keys
    assert pennsylvania_railroad in keys
    assert virginia_avenue in keys


def test_get(pennsylvania_railroad, states_avenue, st_charles_place):
    tile_list = TileList([pennsylvania_railroad, states_avenue, st_charles_place])
    assert tile_list.get(states_avenue) == states_avenue
    assert tile_list.get(pennsylvania_railroad) == pennsylvania_railroad
    assert tile_list.get(states_avenue) == states_avenue
