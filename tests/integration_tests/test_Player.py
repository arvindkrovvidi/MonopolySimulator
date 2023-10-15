import pytest

from errors import PropertyNotFreeError


def test_buy_asset_1(arvind, st_charles_place):
    """
    Test buy_asset when property is free
    """
    assert st_charles_place.owner is None
    arvind.buy_asset(st_charles_place)
    assert st_charles_place.owner is arvind

def test_buy_asset_2(arvind, st_charles_place, arun):
    """
    Test buy_asset when property is not free
    """
    arun.buy_asset(st_charles_place)
    assert st_charles_place.owner == arun
    with pytest.raises(PropertyNotFreeError):
        arvind.buy_asset(st_charles_place)
    assert st_charles_place.owner == arun

def test_pay_rent_property_1(arvind, arun, st_charles_place):
    """
    test pay_rent when player does not own color set or has not built any houses or hotels.
    """
    arun.buy_asset(st_charles_place)
    arvind.pay_rent(arun, st_charles_place.rent)

    assert arvind.cash == 190
    assert arun.cash == 70

def test_pay_rent_property_2(arvind, arun, st_charles_place, virginia_avenue, states_avenue, electric_company):
    """
    test pay_rent when player owns color set
    """
    arun.move_to(electric_company.tile_no, collect_go_cash_flag=True)
    arun.move_to(st_charles_place.tile_no, collect_go_cash_flag=True)
    arun.buy_asset(st_charles_place)
    arun.buy_asset(virginia_avenue)
    arun.buy_asset(states_avenue)
    arvind.pay_rent(arun, st_charles_place.rent)

    assert arvind.cash == 180
    assert arun.cash == 180

def test_pay_rent_property_3(arvind, arun, st_charles_place, virginia_avenue, states_avenue, electric_company):
    """
    test pay_rent when player owns color set and has built a house
    """
    arun.move_to(electric_company.tile_no, collect_go_cash_flag=True)
    arun.move_to(st_charles_place.tile_no, collect_go_cash_flag=True)
    arun.buy_asset(st_charles_place)
    arun.buy_asset(virginia_avenue)
    arun.buy_asset(states_avenue)
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


    arun.buy_asset(st_charles_place)
    arun.buy_asset(virginia_avenue)
    arun.buy_asset(states_avenue)

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

def test_buy_asset_1(arvind, pennsylvania_railroad):
    """
    Test buy_asset function when railroad is free
    """
    assert pennsylvania_railroad.owner is None
    arvind.buy_asset(pennsylvania_railroad)
    assert pennsylvania_railroad.owner == arvind
    assert pennsylvania_railroad in arvind.player_portfolio
    assert arvind.cash == 0
def test_buy_asset_2(arvind, arun, pennsylvania_railroad):
    """
    Test buy_asset function when railroad is not free
    """
    arun.buy_asset(pennsylvania_railroad)
    assert pennsylvania_railroad.owner is arun
    with pytest.raises(PropertyNotFreeError):
        arvind.buy_asset(pennsylvania_railroad)
    assert pennsylvania_railroad.owner == arun
    assert arun.cash == 0
    assert arvind.cash == 200

def test_buy_asset_3(arvind, pennsylvania_railroad, bo_railroad):
    """
    Test buy_asset function for buying multiple railroads
    """
    arvind.move_to(pennsylvania_railroad.tile_no, collect_go_cash_flag=True)

    assert pennsylvania_railroad.owner is None
    assert bo_railroad.owner is None

    arvind.buy_asset(pennsylvania_railroad)
    arvind.buy_asset(bo_railroad)

    assert pennsylvania_railroad.owner is arvind
    assert bo_railroad.owner is arvind
    assert pennsylvania_railroad in arvind.player_portfolio
    assert bo_railroad in arvind.player_portfolio
    assert arvind.cash == 0

def test_buy_asset_1(arvind, electric_company):
    """
    Test buy_asset when utility is free.
    """
    assert electric_company.owner is None
    arvind.buy_asset(electric_company)
    assert electric_company.owner is arvind
    assert arvind.cash == 50

def test_buy_asset_2(arvind, arun, electric_company):
    """
    Test buy_asset when utility is not free
    """
    assert electric_company.owner is None
    arun.buy_asset(electric_company)

    with pytest.raises(PropertyNotFreeError):
        arvind.buy_asset(electric_company)

    assert electric_company.owner == arun
    assert arun.cash == 50
    assert arvind.cash == 200


def test_buy_asset_3(arvind, electric_company, water_works):
    """
    Test buy_asset for buying multiple utilities
    """
    arvind.move_to(electric_company, collect_go_cash_flag=True)
    arvind.buy_asset(electric_company)
    arvind.buy_asset(water_works)

    assert electric_company.owner is arvind
    assert water_works.owner is arvind
    assert electric_company in arvind.player_portfolio
    assert water_works in arvind.player_portfolio
    assert arvind.cash == 100

def test_pay_rent_railroad_1(arvind, arun, pennsylvania_railroad):
    """
    Test pay_rent function for railroads when owner has one railroad.
    """
    assert pennsylvania_railroad.owner is None
    arun.buy_asset(pennsylvania_railroad)
    arvind.pay_rent(arun, pennsylvania_railroad.rent)

    assert arvind.cash == 175
    assert arun.cash == 25

def test_pay_rent_railroad_2(arvind, arun, pennsylvania_railroad, bo_railroad):
    """
    Test pay_rent function for railroads when owner has multiple railroads.
    """
    arun.move_to(pennsylvania_railroad, collect_go_cash_flag=True)
    assert pennsylvania_railroad.owner is None
    assert bo_railroad.owner is None

    arun.buy_asset(pennsylvania_railroad)
    arun.buy_asset(bo_railroad)
    arvind.pay_rent(arun, pennsylvania_railroad.rent)

    assert arvind.cash == 150
    assert arun.cash == 50

def test_pay_rent_utility_1(mocker, arvind, arun, electric_company):
    """
    Test pay_rent function for utilities when owner has one utility.
    """
    assert electric_company.owner is None
    arun.buy_asset(electric_company)
    mocker.patch.object(arvind, 'throw_dice', return_value=5)
    throw = arvind.throw_dice()
    arvind.pay_rent(arun, electric_company.get_rent(throw))

    assert arvind.cash == 180
    assert arun.cash == 70

def test_pay_rent_utility_2(mocker, arvind, arun, electric_company, water_works):
    """
    Test pay_rent function for utilities when owner has one utility.
    """
    arun.move_to(electric_company.tile_no, collect_go_cash_flag=True)
    assert electric_company.owner is None
    assert water_works.owner is None

    arun.buy_asset(electric_company)
    arun.buy_asset(water_works)

    mocker.patch.object(arvind, 'throw_dice', return_value=5)
    throw = arvind.throw_dice()
    arvind.pay_rent(arun, electric_company.get_rent(throw))

    assert arvind.cash == 150
    assert arun.cash == 150