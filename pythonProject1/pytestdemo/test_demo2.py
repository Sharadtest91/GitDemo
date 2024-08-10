import pytest

@pytest.mark.skip
def test_firstprogram():
    msg = "hello"
    assert msg == "HI", "test failed because strings not matched"

@pytest.mark.smoke
def test_creditcard():
    a = 4
    b = 6
    assert a+2 == 6, "addition not matching"




