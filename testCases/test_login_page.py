import pytest

from pageObjects.LoginPage_Objects import LoginPage
from utilities.Logger import LogGenerator
from utilities.Read_Config_File import Read_Confi_File
from utilities.Read_Excel_File import Read_Excel_File


class Test_LoginPage:
    log = LogGenerator.getLog()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.log.info("--------------- Login Page ---------------")
        self.log.info("Login Test is Started")
        self.driver = setup
        self.log.info("Invoking Browser And Opening URL")
        LP = LoginPage(self.driver)
        R = Read_Confi_File()

        LP.email(R.Email())
        self.log.info(f"Entring Email as :: {R.Email()}")
        LP.password(R.Password())
        self.log.info(f"Entring Email as :: {R.Password()}")
        LP.login()
        try:
            t = self.driver.title
            self.log.info(f"Title of Login Page :: {t}")
            if t == "Dashboard / nopCommerce administration":
                self.log.info(f"Login Page Title is passed")
            else:
                self.log.error(f"Login Page Title is failed :: {t}")
                self.driver.get_screenshot_as_file(".//Screenshots//Login Fail.png")
        except Exception as e:
            self.log.info(f"Login Not Possible b'cos of :: {e}")

        self.driver.implicitly_wait(1)
        LP.logout()
        self.driver.close()
        self.log.info("Login Test is Completed")

    @pytest.mark.regression
    def test_login_by_DDT_frame(self, setup):
        self.log.info("--------------- Login Page ---------------")
        self.log.info("Test Login By DDT Frame is Started")
        self.driver = setup
        self.log.info("Invoking Browser And Opening URL")
        LP = LoginPage(self.driver)
        E = Read_Excel_File()

        for i in range(6, 10):
            LP.email(E.read_excel(i, 5))
            self.log.info(f"Entring Email as :: {E.read_excel(i, 5)}")
            LP.password(E.read_excel(i, 6))
            self.log.info(f"Entring Email as :: {E.read_excel(i, 6)}")
            LP.login()
            self.driver.implicitly_wait(2)
            t = self.driver.title
            self.log.info(f"Title of Login Page :: {t}")

            # Test Condictions Cheak Through Valid and Invalid data::
            if t == "Dashboard / nopCommerce administration":
                if E.read_excel(i, 9) == "Pass":
                    self.log.info("Login Success Through Valid Data")
                    E.write_excel(i, 10, "Pass")
                    LP.logout()
                elif E.read_excel(i, 9) == "Fail":
                    self.log.error("Login Success Through Invalid Data")
                    self.driver.get_screenshot_as_file(".//Screenshots//Login Fail.png")
                    E.write_excel(i, 10, "Fail")
                    LP.logout()
            elif t != "Dashboard / nopCommerce administration":
                if E.read_excel(i, 9) == "Pass":
                    self.log.error("Login Failed Through Valid Data")
                    self.driver.get_screenshot_as_file(".//Screenshots//Login Fail.png")
                    E.write_excel(i, 10, "Fail")
                elif E.read_excel(i, 9) == "Fail":
                    self.log.error(f"Login Failed Through Invalid Data")
                    E.write_excel(i, 10, "Fail")
            self.driver.implicitly_wait(1)

            # Finaly Test Status Cheak - (Pass/Fail)
            if E.read_excel(i, 9) == E.read_excel(i, 10):
                E.write_excel(i, 11, "Test Pass")
            elif E.read_excel(i, 9) != E.read_excel(i, 10):
                E.write_excel(i, 11, "Test Fail")

        self.driver.close()
        self.log.info("Test Login By DDT Frame is Completed")
