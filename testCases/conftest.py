from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(r"C:\Users\sande\OneDrive\Desktop\chromedriver.exe")
    elif browser == "firefox":
        driver = webdriver.firefox(r"C:\Users\sande\OneDrive\Desktop\geckodriver.exe")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project name'] = 'nop commerce'
    config._metadata['Module name'] = 'Customers'
    config._metadata['Tester'] = 'Sandesh'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
