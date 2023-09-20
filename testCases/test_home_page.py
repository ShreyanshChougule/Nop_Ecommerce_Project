import pytest

from utilities.Logger import LogGenerator


class Test_HomePage:
    log = LogGenerator.getLog()

    @pytest.mark.sanity
    def test_home_page(self, setup):
        self.log.info("--------------- Home Page ---------------")
        self.log.info("Home Page Test is Started")
        self.driver = setup
        self.log.info("Invoking Browser And Opening URL")
        try:
            t = self.driver.title
            self.log.info(f"Title of Home Page :: {t}")
            if t == "Your store. Login":
                self.log.info(f"Home Page Title is passed")
            else:
                self.log.error(f"Home Page Title is failed :: {t}")
                self.driver.get_screenshot_as_file(".//Screenshots//Home Page Title Fail.png")
        except Exception as e:
            self.log.info(f"Home Page Test Not Possible b'cos of :: {e}")

        self.driver.close()
        self.log.info("Home Page Test is Completed")
