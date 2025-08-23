import os, pytest

def pytest_addoption(parser):
    parser.addoption("--base-json", action="store", default=os.getenv("BASE_JSON", "https://jsonplaceholder.typicode.com"))
    parser.addoption("--base-reqres", action="store", default=os.getenv("BASE_REQRES", "https://reqres.in/api"))

@pytest.fixture(scope="session")
def base_json(pytestconfig):
    return pytestconfig.getoption("--base-json")

@pytest.fixture(scope="session")
def base_reqres(pytestconfig):
    return pytestconfig.getoption("--base-reqres")
