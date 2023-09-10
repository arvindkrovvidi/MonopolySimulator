from Property_data import states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad
from PropertyIterators import PropertyList, PropertyDict
import pytest
from Player_data import arvind, arun


@pytest.fixture
def states_avenue_fx():
    return states_avenue


@pytest.fixture
def st_charles_place_fx():
    return st_charles_place


@pytest.fixture
def virginia_avenue_fx():
    return virginia_avenue


@pytest.fixture
def pennsylvania_railroad_fx():
    return pennsylvania_railroad


@pytest.fixture
def property_list(states_avenue_fx, st_charles_place_fx, pennsylvania_railroad_fx, virginia_avenue_fx):
    ls = PropertyList([states_avenue_fx, st_charles_place_fx, pennsylvania_railroad_fx, virginia_avenue_fx])
    return ls


@pytest.fixture
def arvind_fx():
    return arvind


@pytest.fixture
def arun_fx():
    return arun


@pytest.fixture
def property_dict(states_avenue_fx, st_charles_place_fx, pennsylvania_railroad_fx, virginia_avenue_fx, arvind_fx,
                  arun_fx):
    return PropertyDict({
        states_avenue_fx: arvind_fx,
        st_charles_place_fx: arun_fx,
        pennsylvania_railroad_fx: arvind_fx,
        virginia_avenue_fx: arun_fx
    })