from seasons import Time
from datetime import date
import pytest

def test_get():
    with pytest.raises(SystemExit):
        Time.get("2024/06/28")
    with pytest.raises(SystemExit):
        Time.get("02.08.1996")  
          
def test_minutes():
    t=Time(birthday=date(1994,9,28),today=date(2025,8,12))
    assert Time.minutes(t)==16237440
    
    d=Time(birthday=date(2024,8,12),today=date(2025,8,12))
    assert Time.minutes(d)==525600
    
    
    
    

