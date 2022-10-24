from selenium import webdriver
from time import sleep
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig
from utilities import xlutilities



class Test_002_Login:
    baseUrl = ReadConfig.getUrl()
    path = ".//testdata/login_DDT.xlsx"
    logger = LogGen.log_gen()



    def test_login_ddt(self, setup):
        self.logger.info("********verifying login test*****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Login(self.driver)
        self.rows = xlutilities.getrowcount(self.path, "DDT")

        status_list = []
        for r in range(2, self.rows+1):
            self.user = xlutilities.read_data(self.path, 'DDT', r, 1)
            self.password = xlutilities.read_data(self.path, 'DDT', r, 2)
            self.exp = xlutilities.read_data(self.path, 'DDT', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.click_login()
            sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.lp.click_logout();
                    status_list.append("pass")
                elif self.exp == "fail":
                    self.lp.click_logout();
                    status_list.append("fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    status_list.append("fail")
                elif self.exp == "fail":
                    status_list.append("pass")

        self.driver.close()









