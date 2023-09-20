from selenium.webdriver.common.by import By


class SearchCustomerPage:
    Email = (By.XPATH, "//input[@id='SearchEmail']")
    Firs_tName = (By.ID, "SearchFirstName")
    Last_Name = (By.ID, "SearchLastName")
    Search = (By.XPATH, '//*[@id="search-customers"]/i')

    # Table = (By.XPATH, "//table[@id='customers-grid']")
    # Table_Rows = (By.XPATH, "//table[@id='customers-grid']//tbody/tr")
    # Table_Columns = (By.XPATH, "//table[@id='customers-grid']//tbody/tr/td")

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*SearchCustomerPage.Email).clear()
        self.driver.find_element(*SearchCustomerPage.Email).send_keys(email)

    def set_first_name(self, first_name):
        self.driver.find_element(*SearchCustomerPage.Firs_tName).clear()
        self.driver.find_element(*SearchCustomerPage.Firs_tName).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*SearchCustomerPage.Last_Name).clear()
        self.driver.find_element(*SearchCustomerPage.Last_Name).send_keys(last_name)

    def click_search(self):
        self.driver.find_element(*SearchCustomerPage.Search).click()

    def search_customer_by_email(self, email1):
        A = "False"
        for i in range(1, 9):
            eml = self.driver.find_element(By.XPATH, f"//*[@id='customers-grid']/tbody/tr[{i}]/td[2]").text
            if email1 == eml:
                A = "True"
                break
        return A

    def search_customer_by_name(self, name1):
        B = "False"
        for j in range(1, 9):
            nam = self.driver.find_element(By.XPATH, f"//table[@id='customers-grid']/tbody/tr['{j}']/td[3]").text
            if name1 == nam:
                B = "True"
                break
        return B