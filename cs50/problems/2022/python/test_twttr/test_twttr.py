from twttr_copy import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("ABCDEFG")=="BCDFG"
    assert shorten("hijklmn")=="hjklmn"
    assert shorten("AeiOU")==""
    assert shorten("OpQrStuV")=="pQrStV"
    assert shorten("WYXz")=="WYXz"

