from numb3rs import validate

def test_validate():
    assert validate("0.0.0.0")==True
    assert validate("255.255.255.255")==True
    assert validate("127.0.0.1")==True
    assert validate("255.777.888.999")==False
    assert validate("255.000.789.456")==False
    assert validate("hello,world")==False



