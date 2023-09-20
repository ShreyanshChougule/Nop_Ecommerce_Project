import time

import pytest

from pageObjects.Addcustomer_Objects import AddCustomerPage
from pageObjects.LoginPage_Objects import LoginPage
from pageObjects.SearchCustomer_Objects import SearchCustomerPage
from utilities.Logger import LogGenerator
from utilities.Read_Config_File import Read_Confi_File


class Test_SearchCustomer:
    log = LogGenerator.getLog()

    @pytest.mark.regression
    def test_search_customer_by_email(self, setup):
        self.log.info("--------------- Search Customer ---------------")
        self.driver = setup
        LP = LoginPage(self.driver)
        R = Read_Confi_File()
        A = AddCustomerPage(self.driver)
        S = SearchCustomerPage(self.driver)

        LP.email(R.Email())
        LP.password(R.Password())
        LP.login()
        self.log.info("Login Successful")
        self.driver.implicitly_wait(4)
        self.log.info("Test Search Customer By Email is Started")
        A.click_customers()
        A.click_sub_customers()
        self.driver.implicitly_wait(4)

        # email = "IoKuH@gmail.com"         # # Not Valid Data
        email = "james_pan@nopCommerce.com"
        S.set_email(email)
        S.click_search()

        self.log.info(f"Searching Customer By Email :: {email}")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(7)

        try:
            status = S.search_customer_by_email(email)
            if status == "True":
                self.log.info("Search Email Found in Table")
            else:
                self.log.error("Search Email Not Found in Table")
                self.driver.implicitly_wait(3)
                self.driver.get_screenshot_as_file(".//Screenshots//Search by Email Fail.png")
        except Exception as e:
            self.log.info(f"Serch Not Complet b'cos of :: {e}")

        LP.logout()
        self.log.info("Logout Successful")
        self.driver.close()
        self.log.info("Search Customer By Email Test is Completed")

    @pytest.mark.regression
    def test_search_customer_by_name(self, setup):
        self.log.info("--------------- Search Customer ---------------")
        self.driver = setup
        LP = LoginPage(self.driver)
        R = Read_Confi_File()
        A = AddCustomerPage(self.driver)
        S = SearchCustomerPage(self.driver)

        LP.email(R.Email())
        LP.password(R.Password())
        LP.login()
        self.log.info("Login Successful")
        self.driver.implicitly_wait(4)
        self.log.info("Test Search Customer By Name is Started")
        A.click_customers()
        A.click_sub_customers()
        self.driver.implicitly_wait(4)

        name = "James Pan"
        S.set_first_name(name.split()[0])
        S.set_last_name(name.split()[1])
        S.click_search()

        self.log.info(f"Searching Customer By Name :: {name}")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(7)

        try:
            status = S.search_customer_by_name(name)
            if status == "True":
                self.log.info("Search Name Found in Table")
            else:
                self.log.error("Search Name Not Found in Table")
                self.driver.implicitly_wait(3)
                self.driver.get_screenshot_as_file(".//Screenshots//Search by Name Fail.png")
        except Exception as e:
            self.log.info(f"Serch Test Not Complet b'cos of :: {e}")

        LP.logout()
        self.log.info("Logout Successful")
        self.driver.close()
        self.log.info("Search Customer By Name Test is Completed")
