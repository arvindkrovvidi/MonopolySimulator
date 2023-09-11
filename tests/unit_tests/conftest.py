from Property_data import states_avenue, st_charles_place, virginia_avenue, pennsylvania_railroad
from PropertyIterators import PropertyList, PropertyDict
import pytest
from Player import Player


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
    arvind = Player("Arvind", 200)
    return arvind


@pytest.fixture
def arun_fx():
    arun = Player("Arun", 200)
    return arun


@pytest.fixture
def adityam_fx():
    adityam = Player("Adityam", 200)
    return adityam


@pytest.fixture
def padma_fx():
    padma = Player("Padma", 200)
    return padma


@pytest.fixture
def sree_fx():
    sree = Player("Sree", 200)
    return sree

@pytest.fixture
def property_dict(states_avenue_fx, st_charles_place_fx, pennsylvania_railroad_fx, virginia_avenue_fx, arvind_fx,
                  arun_fx):
    return PropertyDict({
        states_avenue_fx: arvind_fx,
        st_charles_place_fx: arun_fx,
        pennsylvania_railroad_fx: arvind_fx,
        virginia_avenue_fx: arun_fx
    })