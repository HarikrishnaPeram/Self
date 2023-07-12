import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service(executable_path="C:/Users/selenium/work space/chromedriver.exe")
    driver=webdriver.Chrome(service=service_obj)
   # driver = webdriver.Chrome(executable_path="C:/Users/selenium/work space/chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    #driver.get("https://www.facebook.com/signup")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
