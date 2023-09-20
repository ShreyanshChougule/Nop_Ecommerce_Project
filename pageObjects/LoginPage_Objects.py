from selenium.webdriver.common.by import By


class LoginPage:
    Email = (By.ID, "Email")
    Password = (By.ID, "Password")
    Login = (By.XPATH, "//button[@type='submit']")
    Logout = (By.LINK_TEXT, "Logout")

    def __init__(self, driver):
        self.driver = driver

    def email(self, email):
        self.driver.find_element(*LoginPage.Email).clear()
        self.driver.find_element(*LoginPage.Email).send_keys(email)

    def password(self, email):
        self.driver.find_element(*LoginPage.Password).clear()
        self.driver.find_element(*LoginPage.Password).send_keys(email)

    def login(self):
        self.driver.find_element(*LoginPage.Login).click()

    def logout(self):
        self.driver.find_element(*LoginPage.Logout).click()
