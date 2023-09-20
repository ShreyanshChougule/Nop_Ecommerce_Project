import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomerPage:
    Customers = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    Sub_Customers = (By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]")
    Add_Customers = (By.XPATH, "//a[@class='btn btn-primary']")
    Email = (By.XPATH, "//input[@id='Email']")
    Password = (By.XPATH, "//input[@id='Password']")
    First_Name = (By.XPATH, "//input[@id='FirstName']")
    Last_Name = (By.XPATH, "//input[@id='LastName']")
    Male = (By.XPATH, "//input[@id='Gender_Male']")
    Female = (By.XPATH, "//input[@id='Gender_Female']")
    DOB = (By.XPATH, "//input[@id='DateOfBirth']")
    Company = (By.XPATH, "//input[@id='Company']")
    IsTaxExempt = (By.XPATH, "//input[@id='IsTaxExempt']")

    News_Letter = (By.XPATH, '//*[@id="customer-info"]/div[2]/div[9]/div[2]/div/div[1]/div/div')
    Your_Store_Name = (By.XPATH, "//span[normalize-space()='Your store name']")
    Test_Store_2 = (By.XPATH, "//span[normalize-space()='Test store 2']")

    Customer_Roles = (By.XPATH, "//div[@class='k-multiselect-wrap k-floatwrap']")
    Administrators = (By.XPATH, "//li[contains(text(),'Administrators')]")
    Registered = (By.XPATH, "//li[contains(text(),'Registered']")
    Guests = (By.XPATH, "//li[contains(text(),'Guests')]")
    Vendors = (By.XPATH, "//li[contains(text(),'Vendors']")

    VendorID = (By.XPATH, "//select[@id='VendorId']")
    Active = (By.XPATH, "//input[@id='Active']")
    Admin_Comment = (By.XPATH, "//textarea[@id='AdminComment']")
    Save = (By.XPATH, "//button[@name='save']")

    def __init__(self, driver):
        self.driver = driver

    def click_customers(self):
        self.driver.find_element(*AddCustomerPage.Customers).click()

    def click_sub_customers(self):
        self.driver.find_element(*AddCustomerPage.Sub_Customers).click()

    def click_add_customers(self):
        self.driver.find_element(*AddCustomerPage.Add_Customers).click()

    def set_email(self, email):
        self.driver.find_element(*AddCustomerPage.Email).clear()
        self.driver.find_element(*AddCustomerPage.Email).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*AddCustomerPage.Password).clear()
        self.driver.find_element(*AddCustomerPage.Password).send_keys(password)

    def set_first_name(self, first_name):
        self.driver.find_element(*AddCustomerPage.First_Name).clear()
        self.driver.find_element(*AddCustomerPage.First_Name).send_keys(first_name)

    def set_last_name(self, last_name):
        self.driver.find_element(*AddCustomerPage.Last_Name).clear()
        self.driver.find_element(*AddCustomerPage.Last_Name).send_keys(last_name)

    def set_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(*AddCustomerPage.Male).click()
        elif gender == "Female":
            self.driver.find_element(*AddCustomerPage.Female).click()
        else:
            self.driver.find_element(*AddCustomerPage.Male).click()

    def set_Dob(self, DOB):
        self.driver.find_element(*AddCustomerPage.DOB).send_keys(DOB)

    def set_company(self, Company):
        self.driver.find_element(*AddCustomerPage.Company).clear()
        self.driver.find_element(*AddCustomerPage.Company).send_keys(Company)

    def click_tax(self):
        self.driver.find_element(*AddCustomerPage.IsTaxExempt).click()

    def set_news_letter(self, news_letter):
        self.driver.find_element(*AddCustomerPage.News_Letter).click()
        time.sleep(4)
        if news_letter == "Your store name":
            N = self.driver.find_element(*AddCustomerPage.Your_Store_Name)
        elif news_letter == "Test store 2":
            N = self.driver.find_element(*AddCustomerPage.Test_Store_2)
        else:
            N = self.driver.find_element(*AddCustomerPage.Test_Store_2)

        self.driver.execute_script("arguments[0].click();", N)  # This is a JavaScript Statment to Run Code.
        time.sleep(4)

    def set_customer_roles(self, Role):
        self.driver.find_element(*AddCustomerPage.Customer_Roles).click()
        time.sleep(4)
        if Role == "Registered":
            listm = self.driver.find_element(*AddCustomerPage.Registered)
        elif Role == "Administrators":
            listm = self.driver.find_element(*AddCustomerPage.Administrators)
        elif Role == "Guests":
            # Here user can be Registered or Guest, only one
            time.sleep(4)
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            listm = self.driver.find_element(*AddCustomerPage.Guests)
        elif Role == "Registered":
            listm = self.driver.find_element(*AddCustomerPage.Registered)
        elif Role == "Vendors":
            listm = self.driver.find_element(*AddCustomerPage.Vendors)
        else:
            listm = self.driver.find_element(*AddCustomerPage.Guests)
        time.sleep(4)
        # R.click()                                             # This Won't Run tyr Another Way
        self.driver.execute_script("arguments[0].click();", listm)  # This is a JavaScript Statment to Run Code.

    def set_manager_of_vendor(self, vender):
        drp = Select(self.driver.find_element(*AddCustomerPage.VendorID))
        drp.select_by_value(vender)

    def click_active(self):
        self.driver.find_element(*AddCustomerPage.Active).click()

    def set_comments(self, data):
        self.driver.find_element(*AddCustomerPage.Admin_Comment).send_keys(data)

    def click_save(self):
        self.driver.find_element(*AddCustomerPage.Save).click()
