import pytest

from Tiles.Property import Property


@pytest.mark.parametrize("color_set, houses, hotel, expected_rent", [
    (False, 0, False, 10),
    (False, 0, True, 10),
    (False, 1, False, 10),
    (False, 1, True, 10),
    (True, 0, False, 20),
    (True, 0, True, 20),
    (True, 1, False, 50),
    (True, 1, True, 750),
])
def test_rent(st_charles_place, color_set, houses, hotel, expected_rent):
    st_charles_place._color_set = color_set
    st_charles_place._houses = houses
    st_charles_place._hotel = hotel
    assert st_charles_place.rent == expected_rent


def test_str(states_avenue):
    assert str(states_avenue) == "States Avenue"


def test_eq(states_avenue, property_rent_data):
    test_property = Property(13, "States Avenue", 140, property_rent_data["States Avenue"]["Rent"], "Pink", 100)
    assert test_property == states_avenue