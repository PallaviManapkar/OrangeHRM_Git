from selenium.webdriver.support.wait import WebDriverWait
from utilities.Logger import LogGenerator
from pageObjects.LoginPage import OrangeHRM_Login
from utilities.ReadConfig import ReadConfigs

import allure
from allure_commons.types import AttachmentType


class Test_Login:
    log = LogGenerator.loggen()
    Uname = ReadConfigs.GetUsername()
    Passwrd = ReadConfigs.GetPassword()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Page Title Test Case 001")
    @allure.link("https://opensource-demo.orangehrmlive.com/")
    @allure.issue("IssueNo-225")
    @allure.story("This is story #01")
    def test_page_title_001(self, setup):
        self.log.info("Testcase test_page_title_001 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.log.info("Page Title is " + self.driver.title)

        if self.driver.title == "OrangeHRM":
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_page_title_oo1_pass",attachment_type=AttachmentType.PNG)

            self.driver.save_screenshot(".\\ScreenShots\\test_page_title_001_pass.png")
            self.driver.close()
            self.log.info("Testcase test_page_title_001 is passed")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_page_title_001_fail.png")
            self.log.info("Testcase test_page_title_001 is Failed")
            assert False

    def test_login_001(self, setup):
        self.log.info("Testcase test_login_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lp = OrangeHRM_Login(self.driver)
        self.log.info("Entering Username :")
        # self.lp.Enter_Username("Admin")
        self.lp.Enter_Username(self.Uname)
        self.log.info("Entering Password :")
        # self.lp.Enter_Password("admin123")
        self.lp.Enter_Password(self.Passwrd)
        self.log.info("Clicking on Login Button")
        self.lp.Click_Login()
        self.log.info("Checking Login Status")

        if self.lp.Login_Status() == True:
            self.log.info("Taking Screenshot")
            allure.attach(self.driver.get_screenshot_as_png(),name="test_login_pass",attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot(".\\ScreenShots\\test_login_002_pass.png")
            self.log.info("Clicking on Menu Button")
            self.lp.Click_Menu()
            self.log.info("Clicking on Logout Button")
            self.lp.Click_Logout_Button()
            self.driver.close()
            self.log.info("Testcase test_login_002 is passed")
            assert True
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_login_002_fail.png")
            self.driver.close()
            self.log.info("Testcase test_login_002 is failed")
            assert False

# pytest -v -s --html=HTML_Reports/OrangeHRM_R2.html --alluredir="Allure-Reports"