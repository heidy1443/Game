import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("3/4")==75
    assert convert("4/4")==100
    assert convert("0/4")==0

def test_gauge():
    assert gauge(0)=="E"
    assert gauge(100)=="F"
    assert gauge(75)=="75%"
    

def test_error():
    with pytest.raises(ValueError):
        convert("-5/-2")
    with pytest.raises(ValueError):
        convert("5/3")
    
    with pytest.raises(ZeroDivisionError):
        convert("1/0")