import pytest

@pytest.mark.xfail
def test_firstprogram():
    print("Hello")

@pytest.mark.smoke
def test_creditcard():
    print("whats up")


def test_crossbrowsers(crossbrowsers):
    print(crossbrowsers[1])

