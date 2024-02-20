from selenium.webdriver.common.by import By
from POMProject.Locators.locators import Locators

class LoginPage():

    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_CSS = Locators.login_button_CSS
        self.invalidUsername_message_CSS = Locators.invalidUsername_message_CSS


    def enter_username(self,username):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME, self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR,self.login_button_CSS).click()

    def check_invalid_username(self):
        msg = self.driver.find_element(By.CSS_SELECTOR, self.invalidUsername_message_CSS).text
        return msg





