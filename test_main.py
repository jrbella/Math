from main import powa, is_operator

def test_powa():
    assert powa(2, 2) == 4
    assert powa(2,4) == 16

def test_is_operator():
    assert is_operator('+') == True
    assert is_operator('-') == True
    assert is_operator('/') == True
    assert is_operator('*') == True
    