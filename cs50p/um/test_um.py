from um import count

def test_words():
    assert count("The umbrella is red.")==0
    assert count("This is my favorite album.")==0
    
def test_um():
    assert count("um,um,um,um...")==4
    assert count("Well, this is um, I don't know...um")==2
    
def test_case():
    assert count("Um,good morning.")==1
    assert count("Um, my umbrella is not here.")==1



