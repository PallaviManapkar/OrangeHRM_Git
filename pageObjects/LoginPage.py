from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class OrangeHRM_Login:
    object_username = (By.NAME, "username")
    object_password = (By.NAME, "password")
    object_login_button = (By.XPATH, "//button[@type='submit']")
    object_menu_button = (By.XPATH, "//p[@class='oxd-userdropdown-name']")
    object_logout_button = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Enter_Username(self, username):
        self.wait.until(expected_conditions.visibility_of_element_located(self.object_username))
        self.driver.find_element(*OrangeHRM_Login.object_username).send_keys(username)

    def Enter_Password(self, password):
        self.wait.until(expected_conditions.visibility_of_element_located(self.object_password))
        self.driver.find_element(*OrangeHRM_Login.object_password).send_keys(password)

    def Click_Login(self):
        # self.wait.until(expected_conditions.visibility_of_element_located(self.object_login_button))
        self.driver.find_element(*OrangeHRM_Login.object_login_button).click()

    def Click_Menu(self):
        # self.wait.until(expected_conditions.visibility_of_element_located(self.object_menu_button))
        self.driver.find_element(*OrangeHRM_Login.object_menu_button).click()

    def Click_Logout_Button(self):
        self.wait.until(expected_conditions.visibility_of_element_located(self.object_logout_button))
        self.driver.find_element(*OrangeHRM_Login.object_logout_button).click()

    def Login_Status(self):
        try:
            self.wait.until((expected_conditions.visibility_of_element_located(self.object_menu_button)))
            self.driver.find_element(*OrangeHRM_Login.object_menu_button)
            return True
        except:
            return False
