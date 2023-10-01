from Property_data import states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad
from TileIterators import TileDict, TileList


def test_tile_list_get_item(property_list, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                            pennsylvania_railroad_fx):
    assert property_list[11] == st_charles_place
    assert property_list[13] == states_avenue
    assert property_list[14] == virginia_avenue
    assert property_list[15] == pennsylvania_railroad


def test_tile_list_next(property_list, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                        pennsylvania_railroad_fx):
    for asset in property_list:
        print(asset)


def test_tile_list_contains(property_list, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                            pennsylvania_railroad_fx):
    assert states_avenue_fx in property_list
    assert st_charles_place_fx in property_list
    assert pennsylvania_railroad_fx in property_list
    assert virginia_avenue_fx in property_list


def test_tile_list_append(st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                          pennsylvania_railroad_fx):
    property_list = TileList([st_charles_place_fx, states_avenue_fx])
    property_list.append(virginia_avenue_fx)
    assert virginia_avenue_fx in property_list
    property_list.append(pennsylvania_railroad_fx)
    assert pennsylvania_railroad_fx in property_list


def test_tile_dict_get_item(property_dict, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                            pennsylvania_railroad_fx, arvind_fx, arun_fx):
    assert property_dict[states_avenue_fx] == arvind_fx
    assert property_dict[st_charles_place_fx] == arun_fx
    assert property_dict[pennsylvania_railroad_fx] == arvind_fx
    assert property_dict[virginia_avenue_fx] == arun_fx


def test_tile_dict_next_item(property_dict, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                             pennsylvania_railroad_fx):
    try:
        while True:
            next(property_dict)
    except StopIteration:
        pass


def test_tile_dict_contains(property_dict, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                            pennsylvania_railroad_fx):
    assert states_avenue_fx in property_dict
    assert st_charles_place_fx in property_dict
    assert pennsylvania_railroad_fx in property_dict
    assert virginia_avenue_fx in property_dict


def test_tile_dict_update(st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                          pennsylvania_railroad_fx, arvind_fx, arun_fx):
    property_dict = TileDict({st_charles_place_fx: arvind_fx,
                              states_avenue_fx: arun_fx
                              })
    property_dict.update_dict({pennsylvania_railroad_fx: arvind_fx})
    assert pennsylvania_railroad_fx in property_dict
    assert property_dict[pennsylvania_railroad_fx] == arvind_fx
    property_dict.update_dict({virginia_avenue_fx: arun_fx})
    assert virginia_avenue_fx in property_dict
    assert property_dict[virginia_avenue_fx] == arun_fx


def test_add(arvind_fx, arun_fx, padma_fx, adityam_fx):
    list1 = TileList([arvind_fx, arun_fx])
    list2 = TileList([adityam_fx, padma_fx])
    actual = list1 + list2
    assert type(actual) == TileList
    assert arvind_fx in actual
    assert arun_fx in actual
    assert adityam_fx in actual
    assert padma_fx in actual


def test_keys(arvind_fx, arun_fx, adityam_fx, padma_fx, states_avenue_fx, st_charles_place_fx, pennsylvania_railroad_fx,
              virginia_avenue_fx):
    tile_dict = TileDict({states_avenue_fx: arvind_fx,
                          st_charles_place_fx: arun_fx,
                          pennsylvania_railroad_fx: adityam_fx,
                          virginia_avenue_fx: padma_fx})
    keys = tile_dict.keys()
    assert states_avenue_fx in keys
    assert st_charles_place_fx in keys
    assert pennsylvania_railroad_fx in keys
    assert virginia_avenue_fx in keys


def test_get(pennsylvania_railroad_fx, states_avenue_fx, st_charles_place_fx):
    tile_list = TileList([pennsylvania_railroad_fx, states_avenue_fx, st_charles_place_fx])
    assert tile_list.get(states_avenue_fx) == states_avenue_fx
    assert tile_list.get(pennsylvania_railroad_fx) == pennsylvania_railroad
    assert tile_list.get(states_avenue_fx) == states_avenue_fx


def test_copy(arvind_fx, arun_fx, adityam_fx, padma_fx):
    players = TileList([arvind_fx, arun_fx, adityam_fx, padma_fx])
    other_players = players.copy()
    assert arvind_fx in other_players
    assert arun_fx in other_players
    assert padma_fx in other_players
    assert adityam_fx in other_players
