from selenium.webdriver.common.by import By
from POMProject.Locators.locators import Locators
class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_link_CSS = Locators.welcome_link_CSS
        self.logout_link_linktext = Locators.logout_link_linktext

    def click_welcome(self):
        self.driver.find_element(By.CSS_SELECTOR, self.welcome_link_CSS).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linktext).click()