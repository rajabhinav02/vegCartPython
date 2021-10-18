import pytest
from selenium import webdriver

from testdata.TestDataExcel import TestData


def pytest_addoption(parser):
    parser.addoption("--browser_name" , action = "store", default = "chrome")
    parser.addoption("--channel_name", action = "store", default = "prod")

@pytest.fixture(scope="class")
def setup(request):
    browsername = request.config.getoption("--browser_name")
    channelname = request.config.getoption("--channel_name")
    urlp = "https://rahulshettyacademy.com/seleniumPractise/#/"
    urle = "https://www.google.com"

    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path= "C:\\chromedriver_win32\\chromedriver.exe")
        driver.maximize_window()
        if channelname == "prod":
            driver.get(urlp)
        elif channelname == "ete":
            driver.get(urle)
    elif browsername == "edge":
        driver = webdriver.Edge(executable_path="C:\\edgedriver_win64\\msedgedriver.exe")
        driver.maximize_window()
        if channelname == "prod":
            driver.get(urlp)
        elif channelname == "ete":
            driver.get(urle)
    if request.cls is not None:
        request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(params= TestData.testdataa("test_fruitorder"))
def testfruit(request):
    return request.param