from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseUrl = ReadConfig.getUrl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.log_gen()

    def test_homepageTitle(self, setup):
        self.logger.info("************Test_001 Login*******************")
        self.logger.info("********verifying homepage title*****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("*********home page title passed*******************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(r".//Screenshots//"+"test_homepageTitle.png")
            self.logger.error("**********home page title failed*****************")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("********verifying login test*****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.click_login()
        self.driver.close()