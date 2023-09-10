from PropertyIterators import PropertyDict, PropertyList
from Property_data import states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad


def test_property_list_get_item(property_list, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                                pennsylvania_railroad_fx):
    assert property_list[8] == st_charles_place
    assert property_list[9] == states_avenue
    assert property_list[10] == virginia_avenue
    assert property_list[11] == pennsylvania_railroad


def test_property_list_next(property_list, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                            pennsylvania_railroad_fx):
    for asset in property_list:
        print(asset)


def test_property_list_contains(property_list, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                                pennsylvania_railroad_fx):
    assert states_avenue_fx in property_list
    assert st_charles_place_fx in property_list
    assert pennsylvania_railroad_fx in property_list
    assert virginia_avenue_fx in property_list


def test_property_list_append(st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                              pennsylvania_railroad_fx):
    property_list = PropertyList([st_charles_place_fx, states_avenue_fx])
    property_list.append(virginia_avenue_fx)
    assert virginia_avenue_fx in property_list
    property_list.append(pennsylvania_railroad_fx)
    assert pennsylvania_railroad_fx in property_list


def test_property_dict_get_item(property_dict, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                                pennsylvania_railroad_fx, arvind_fx, arun_fx):
    assert property_dict[states_avenue_fx] == arvind_fx
    assert property_dict[st_charles_place_fx] == arun_fx
    assert property_dict[pennsylvania_railroad_fx] == arvind_fx
    assert property_dict[virginia_avenue_fx] == arun_fx


def test_property_dict_next_item(property_dict, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                                 pennsylvania_railroad_fx):
    try:
        while True:
            next(property_dict)
    except StopIteration:
        pass


def test_property_dict_contains(property_dict, st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                                pennsylvania_railroad_fx):
    assert states_avenue_fx in property_dict
    assert st_charles_place_fx in property_dict
    assert pennsylvania_railroad_fx in property_dict
    assert virginia_avenue_fx in property_dict


def test_property_dict_update(st_charles_place_fx, states_avenue_fx, virginia_avenue_fx,
                              pennsylvania_railroad_fx, arvind_fx, arun_fx):
    property_dict = PropertyDict({st_charles_place_fx: arvind_fx,
                                  states_avenue_fx: arun_fx
                                  })
    property_dict.update_dict({pennsylvania_railroad_fx: arvind_fx})
    assert pennsylvania_railroad_fx in property_dict
    assert property_dict[pennsylvania_railroad_fx] == arvind_fx
    property_dict.update_dict({virginia_avenue_fx: arun_fx})
    assert virginia_avenue_fx in property_dict
    assert property_dict[virginia_avenue_fx] == arun_fx
