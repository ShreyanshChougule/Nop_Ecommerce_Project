from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(2)
t = driver.title
driver.get_screenshot_as_file("Name")
driver.execute_script("arguments[0].click();", "R")
m = driver.find_element(By.TAG_NAME, "body").text
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")