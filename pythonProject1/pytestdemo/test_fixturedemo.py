import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturedemo(self):
        print("i will execute steps in fixture demo")

    def test_fixturedemo1(self):
        print("i will execute steps in fixture demo1")

    def test_fixturedemo2(self):
        print("i will execute steps in fixture demo2")

    def test_fixturedemo3(self):
        print("i will execute steps in fixture demo3")