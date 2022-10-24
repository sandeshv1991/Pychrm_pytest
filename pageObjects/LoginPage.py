import selenium
from selenium import webdriver


class Login:
    txt_box_username_id = "Email"
    txt_box_password_name = "Password"
    button_login_xpath = "//button[text()='Log in']"
    button_logout_xpath = "//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element_by_id(self.txt_box_username_id).clear()
        self.driver.find_element_by_id(self.txt_box_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_name(self.txt_box_password_name).clear()
        self.driver.find_element_by_name(self.txt_box_password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()
