from plates import is_valid

def test_len():
    assert is_valid("AA2345")==True
    assert is_valid("Hello")==True
    assert is_valid("H")==False
    assert is_valid("Helloworld")==False

def test_alpha():
    assert is_valid("AA2345")==True
    assert is_valid("Hello")==True
    assert is_valid("123456")==False
    assert is_valid("66AAB")==False

def test_special():
    assert is_valid("AA345")==True
    assert is_valid("Halo")==True
    assert is_valid("HH@1 2")==False
    assert is_valid("H^*#")==False

def test_number_position():
    assert is_valid("AA2345")==True
    assert is_valid("Hel33")==True
    assert is_valid("CS5P50")==False
    assert is_valid("AKA021")==False