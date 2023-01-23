
from fotmob.api import FotMobApi

api = FotMobApi()

def test_date_true():
    assert api.checkDate("20210904") == True

def test_date_false():
    assert api.checkDate("09042021") == False
