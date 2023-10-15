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

def test_pay_rent_property_1(arvind, arun, st_charles_place):
    """
    test pay_rent when player does not own color set or has not built any houses or hotels.
    """
    arun.buy_property(st_charles_place)
    arvind.pay_rent(arun, st_charles_place.rent)

    assert arvind.cash == 190
    assert arun.cash == 70

def test_pay_rent_property_2(arvind, arun, st_charles_place, virginia_avenue, states_avenue, electric_company):
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

def test_pay_rent_property_3(arvind, arun, st_charles_place, virginia_avenue, states_avenue, electric_company):
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

def test_pay_rent_property_4(arvind, arun, st_charles_place, virginia_avenue, states_avenue, electric_company):
    """
    test pay_rent when player owns color set and has built a house and a hotel
    """
    arun.cash = 1000
    arvind.cash = 1000

    arun.move_to(electric_company.tile_no, collect_go_cash_flag=True)
    arun.move_to(st_charles_place.tile_no, collect_go_cash_flag=True)
    arun.move_to(st_charles_place.tile_no, collect_go_cash_flag=True)
    arun.move_to(st_charles_place.tile_no, collect_go_cash_flag=True)
    arun.move_to(st_charles_place.tile_no, collect_go_cash_flag=True)
    arun.move_to(st_charles_place.tile_no, collect_go_cash_flag=True)


    arun.buy_property(st_charles_place)
    arun.buy_property(virginia_avenue)
    arun.buy_property(states_avenue)

    arun.build_house(st_charles_place)
    arun.build_house(virginia_avenue)
    arun.build_house(states_avenue)
    arun.build_house(st_charles_place)
    arun.build_house(virginia_avenue)
    arun.build_house(states_avenue)
    arun.build_house(st_charles_place)
    arun.build_house(virginia_avenue)
    arun.build_house(states_avenue)
    arun.build_house(st_charles_place)
    arun.build_house(virginia_avenue)
    arun.build_house(states_avenue)

    arun.build_hotel(st_charles_place)
    arvind.pay_rent(arun, st_charles_place.rent)

    assert arvind.cash == 250
    assert arun.cash == 1210

def test_buy_railroad_1(arvind, pennsylvania_railroad):
    """
    Test buy_railroad function when railroad is free
    """
    assert pennsylvania_railroad.owner is None
    arvind.buy_railroad(pennsylvania_railroad)
    assert pennsylvania_railroad.owner == arvind
    assert pennsylvania_railroad in arvind.player_portfolio
def test_buy_railroad_2(arvind, arun, pennsylvania_railroad):
    """
    Test buy_railroad function when railroad is not free
    """
    arun.buy_railroad(pennsylvania_railroad)
    assert pennsylvania_railroad.owner is arun
    with pytest.raises(PropertyNotFreeError):
        arvind.buy_railroad(pennsylvania_railroad)
    assert pennsylvania_railroad.owner == arun

def test_buy_railroad_3(arvind, pennsylvania_railroad, bo_railroad):
    """
    Test buy_railroad function for buying multiple railroads
    """
    arvind.move_to(pennsylvania_railroad.tile_no, collect_go_cash_flag=True)

    assert pennsylvania_railroad.owner is None
    assert bo_railroad.owner is None

    arvind.buy_railroad(pennsylvania_railroad)
    arvind.buy_railroad(bo_railroad)

    assert pennsylvania_railroad.owner is arvind
    assert bo_railroad.owner is arvind
    assert pennsylvania_railroad in arvind.player_portfolio
    assert bo_railroad in arvind.player_portfolio

def test_buy_utility_1(arvind, electric_company):
    """
    Test buy_utility when utility is free.
    """
    assert electric_company.owner is None
    arvind.buy_utility(electric_company)
    assert electric_company.owner is arvind

def test_buy_utility_2(arvind, arun, electric_company):
    """
    Test buy_utility when utility is not free
    """
    assert electric_company.owner is None
    arun.buy_utility(electric_company)

    with pytest.raises(PropertyNotFreeError):
        arvind.buy_utility(electric_company)

    assert electric_company.owner == arun


def test_buy_utility_3(arvind, electric_company, water_works):
    """
    Test buy_utility for buying multiple utilities
    """
    arvind.move_to(electric_company, collect_go_cash_flag=True)
    arvind.buy_utility(electric_company)
    arvind.buy_utility(water_works)

    assert electric_company.owner is arvind
    assert water_works.owner is arvind
    assert electric_company in arvind.player_portfolio
    assert water_works in arvind.player_portfolio