import pytest
from py.xml import html
from seleniumbase import Driver


driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        driver = Driver(browser="chrome", headless=False)
        driver.maximize_window()

    def fn():
        driver.quit()

    request.addfinalizer(fn)
    return driver
