import pytest

from errors import PropertyNotFreeError


def test_buy_property_1(arvind, st_charles_place):
    """
    Test buy_property when property is free
    """
    assert st_charles_place.owner is None
    arvind.buy_property(st_charles_place)
    assert st_charles_place.owner is arvind

def test_buy_property_2(arvind, st_charles_place, arun):
    """
    Test buy_property when property is not free
    """
    arun.buy_property(st_charles_place)
    assert st_charles_place.owner == arun
    with pytest.raises(PropertyNotFreeError):
        arvind.buy_property(st_charles_place)
    assert st_charles_place.owner == arun

def test_pay_rent_1(arvind, arun, st_charles_place):
    """
    test pay_rent when player does not own color set or has not built any houses or hotels.
    """
    arun.buy_property(st_charles_place)
    arvind.pay_rent(arun, st_charles_place.rent)

    assert arvind.cash == 190
    assert arun.cash == 70

def test_pay_rent_2(arvind, arun, st_charles_place, virginia_avenue, states_avenue, electric_company):
    """
    test pay_rent when player owns color set
    """
    arun.move_to(electric_company.tile_no, collect_go_cash_flag=True)
    arun.move_to(st_charles_place.tile_no, collect_go_cash_flag=True)
    arun.buy_property(st_charles_place)
    arun.buy_property(virginia_avenue)
    arun.buy_property(states_avenue)
    arvind.pay_rent(arun, st_charles_place.rent)

    assert arvind.cash == 180
    assert arun.cash == 180

def test_pay_rent_3(arvind, arun, st_charles_place, virginia_avenue, states_avenue, electric_company):
    """
    test pay_rent when player owns color set and has built a house
    """
    arun.move_to(electric_company.tile_no, collect_go_cash_flag=True)
    arun.move_to(st_charles_place.tile_no, collect_go_cash_flag=True)
    arun.buy_property(st_charles_place)
    arun.buy_property(virginia_avenue)
    arun.buy_property(states_avenue)
    arun.build_house(st_charles_place)
    arvind.pay_rent(arun, st_charles_place.rent)

    assert arvind.cash == 150
    assert arun.cash == 110
