from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Baseclass import BaseClass


class Testone(BaseClass):
    def test_e2e(self):
        self.driver.find_element(By.XPATH,"//input[@class='form-control ng-untouched ng-pristine ng-invalid']").send_keys("Harikrishna")
        self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("harikrishnaperam2@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='exampleInputPassword1']").send_keys("Harikrishna2@")
        self.driver.find_element(By.CSS_SELECTOR, "#exampleCheck1").click()
        dropdown1= Select(self.driver.find_element(By.XPATH,"//select[@id='exampleFormControlSelect1']"))
        dropdown1.select_by_index(1)
        self.driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
        self.driver.find_element(By.XPATH,"//input[@id='inlineRadio1']").click()
        #SuccesText=driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
        #assert "Success! Thank you!" in SuccesText


