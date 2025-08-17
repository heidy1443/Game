from jar import Jar
import pytest

def test_init():
    jar=Jar(5,12)
    assert jar.capacity==12
    assert jar.size==5
        
    with pytest.raises(ValueError):
        Jar(13,10)
    
    with pytest.raises(ValueError):
        Jar(5,-10)
        

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪"*12
    jar.withdraw(2)
    assert str(jar) =="🍪"*10
    jar.withdraw(5)
    assert str(jar) =="🍪"*5


def test_deposit():
    jar=Jar(0,5)
    jar.deposit(3)
    assert jar.size==3
    
    with pytest.raises(ValueError):
        jar.deposit(3)
        
def test_withdraw():
    jar=Jar(3,5)
    jar.withdraw(2)
    assert jar.size==1
    
    with pytest.raises(ValueError):
        jar.withdraw(3)
        