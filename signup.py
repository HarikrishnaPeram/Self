from selenium.webdriver.common.by import By


class SignUp:

    def __init__(self, driver):
        self.driver = driver

    firstname = (By.Xpath, "//input[@name='firstname']")
    surname = (By.XPATH, "//input[@id='u_0_d_my']")
    mobileoremail = (By.XPATH, "//input[@id='u_0_g_MR']")
    newpassword = (By.XPATH, "//input[@id='password_step_input']")
    day = (By.XPATH, "#day")
    month = (By.XPATH, "#month")
    year = (By.XPATH, "#year")
    gender = (By.CSS_SELECTOR, "#u_0_5_hS")
    signup = (By.CSS_SELECTOR, "#u_0_s_9H")


    def getfirstname(self):
        return self.driver.find_element(*SignUp.firstname)
    def getsurname(self):
        return self.driver.find_element(*SignUp.surname)

    def getmobileoremail(self):
        return self.driver.find_element(*SignUp.mobileoremail)

    def getnewpassword(self):
        return self.driver.find_element(*SignUp.newpassword)

    def getday(self):
        return self.driver.find_element(*SignUp.day)

    def getmonth(self):
        return self.driver.find_element(*SignUp.month)

    def getyear(self):
        return self.driver.find_element(*SignUp.year)
    def getgender(self):
        return self.driver.find_element(*SignUp.gender)
    def getsignup(self):
        return self.driver.find_element(*SignUp.signup)


