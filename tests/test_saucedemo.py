import time
from selenium.webdriver.common.by import By

def test_internet_site(driver):
    driver.get("https://the-internet.herokuapp.com/")
    driver.maximize_window()

    driver.find_element(By.XPATH, "//a[contains(text(),'A/B Testing')]").click()
    driver.back()

    driver.find_element(By.XPATH, "//a[contains(text(),'Broken Images')]").click()
    driver.back()

    driver.find_element(By.XPATH, "//a[contains(text(),'Checkboxes')]").click()
    driver.back()

