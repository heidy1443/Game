from bank import value

def test_hello():
    assert value("hello,cat!")==0
    assert value("Hello,my baby!")==0

def test_h():
    assert value("How is yor day?")==20
    assert value("hi,nice to meet you!")==20

def test_other():
    assert value("What's up?")==100
    assert value("Are you ok?")==100
