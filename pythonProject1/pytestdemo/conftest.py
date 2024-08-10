import pytest


@pytest.fixture(scope="class")
def setup():
    print("i will be executed first")
    yield
    print("i will execute last")

@pytest.fixture()
def dataload():
    print("user profile will be created")
    return ["rahul", "shetty", "rahulshettyacademy.com"]

@pytest.fixture(params=[("Chrome", "Rahul", "QA"),("Firefox", "Shetty"),("IE", "SSDD")])
def crossbrowsers(request):
    return request.param
