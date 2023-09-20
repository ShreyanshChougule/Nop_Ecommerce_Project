import pytest
from selenium import webdriver
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
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        Chrome_options = webdriver.ChromeOptions()
        Chrome_options.add_argument("headless")
        driver = webdriver.Edge(options=Chrome_options)

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
