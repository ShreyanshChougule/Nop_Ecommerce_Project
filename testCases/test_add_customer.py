import random
import string

import pytest
from selenium.webdriver.common.by import By

from pageObjects.Addcustomer_Objects import AddCustomerPage
from pageObjects.LoginPage_Objects import LoginPage
from utilities.Logger import LogGenerator
from utilities.Read_Config_File import Read_Confi_File


class Test_AddCustomer:
    log = LogGenerator.getLog()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self, setup):
        self.log.info("--------------- Add Customer ---------------")
        self.driver = setup
        LP = LoginPage(self.driver)
        R = Read_Confi_File()
        A = AddCustomerPage(self.driver)

        LP.email(R.Email())
        LP.password(R.Password())
        LP.login()
        self.log.info("Login Successful")
        self.driver.implicitly_wait(4)
        self.log.info("Add Customer Test is Started")
        A.click_customers()
        A.click_sub_customers()
        self.driver.implicitly_wait(4)
        A.click_add_customers()
        self.driver.implicitly_wait(4)

        self.log.info("Providing Customer info.")
        email = f"{email_gen()}@gmail.com"
        A.set_email(email)
        A.set_password("1234")
        A.set_first_name("ABC")
        A.set_last_name("XYZ")
        A.set_gender("Male")
        A.set_Dob("01/13/1993")         # MM/DD/YYYY
        A.set_company("Food Hunters")
        A.click_tax()
        # A.set_news_letter("Your store name")
        # A.set_customer_roles("Guests")
        A.set_manager_of_vendor("1")
        A.click_active()
        A.set_comments("Automation Testing")
        self.driver.implicitly_wait(4)
        A.click_save()
        self.log.info("Saving Customer info.")
        try:
            Message = self.driver.find_element(By.TAG_NAME, "body").text            # This will Capture all info displayed on page.
            self.driver.implicitly_wait(4)
            if "customer has been added successfully." in Message:
                self.log.info("Customer Added Successfully.")
            else:
                self.driver.get_screenshot_as_file(".//Screenshots//Add Customer Fail.png")
                self.log.error("Customer Not Added..!")
        except Exception as e:
            self.log.info(f"Add Cuctomer Test Not Possible b'cos of :: {e}")

        LP.logout()
        self.log.info("Logout Successful")
        self.driver.close()
        self.log.info("Login Test is Completed")


# To Generate Random Eamils::
def email_gen():
    c = string.ascii_lowercase + string.digits
    return "".join(random.choice(c) for _ in range(9))
