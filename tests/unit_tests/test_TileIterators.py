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
                            pennsylvania_railroad, arvind, arun):
    assert property_dict[states_avenue] == arvind
    assert property_dict[st_charles_place] == arun
    assert property_dict[pennsylvania_railroad] == arvind
    assert property_dict[virginia_avenue] == arun


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
                          pennsylvania_railroad, arvind, arun):
    property_dict = TileDict({st_charles_place: arvind,
                              states_avenue: arun
                              })
    property_dict.update_dict({pennsylvania_railroad: arvind})
    assert pennsylvania_railroad in property_dict
    assert property_dict[pennsylvania_railroad] == arvind
    property_dict.update_dict({virginia_avenue: arun})
    assert virginia_avenue in property_dict
    assert property_dict[virginia_avenue] == arun


def test_add(arvind, arun, padma, adityam):
    list1 = TileList([arvind, arun])
    list2 = TileList([adityam, padma])
    actual = list1 + list2
    assert type(actual) == TileList
    assert arvind in actual
    assert arun in actual
    assert adityam in actual
    assert padma in actual


def test_keys(arvind, arun, adityam, padma, states_avenue, st_charles_place, pennsylvania_railroad,
              virginia_avenue):
    tile_dict = TileDict({states_avenue: arvind,
                          st_charles_place: arun,
                          pennsylvania_railroad: adityam,
                          virginia_avenue: padma})
    keys = tile_dict.keys()
    assert states_avenue in keys
    assert st_charles_place in keys
    assert pennsylvania_railroad in keys
    assert virginia_avenue in keys


def test_get(pennsylvania_railroad, states_avenue, st_charles_place):
    tile_list = TileList([pennsylvania_railroad, states_avenue, st_charles_place])
    assert tile_list.get_by_name(str(states_avenue)) == states_avenue
    assert tile_list.get_by_name(str(pennsylvania_railroad)) == pennsylvania_railroad
    assert tile_list.get_by_name(str(states_avenue)) == states_avenue


def test_remove(st_charles_place, states_avenue, virginia_avenue):
    tile_list = TileList([st_charles_place,states_avenue, virginia_avenue])
    tile_list.remove(st_charles_place)
    assert type(tile_list) == TileList
    assert st_charles_place not in tile_list
    assert states_avenue in tile_list
    assert virginia_avenue in tile_list
