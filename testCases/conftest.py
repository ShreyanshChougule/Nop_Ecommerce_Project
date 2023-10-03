import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.Read_Config_File import Read_Confi_File


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# @pytest.yield_fixture()
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser == 'edge':
        # driver = webdriver.Edge()
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    else:
        Chrome_options = webdriver.ChromeOptions()
        Chrome_options.add_argument("headless")
        # driver = webdriver.Chrome(options=Chrome_options)
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=Chrome_options)

    # driver.get("https://admin-demo.nopcommerce.com/login")
    R = Read_Confi_File()
    driver.get(R.URL())
    driver.maximize_window()
    return driver


# # -------------- Pytest HTML Reports --------------
#
# def pytest_congigure(config):
#     config._metadata["Project Name"] = "Nop Commerce"
#     config._metadata["Module Name"] = "Customers"
#     config._metadata["Tester Name"] = "Shreyansh"
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
