# Create a simple login test
import os.path

import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"...","..."))
from POMProject.pages.loginpage import LoginPage
from POMProject.pages.homepage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        service_obj = Service("/Users/Yusuf/PycharmProjects/driver/msedgedriver.exe")
        cls.driver = webdriver.Edge(service = service_obj)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):

        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(self.driver)

        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(self.driver)
        homepage.click_welcome()
        homepage.click_logout()

    def test_login_invalid_username(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(self.driver)

        login.enter_username("Ad")
        login.enter_password("admin123")
        login.click_login()

        message = login.check_invalid_username()
        print(message)
        self.assertEqual(message, "Invalid credentials123")


        # self.driver.find_element(By.NAME, "username").send_keys("Admin")
        # self.driver.find_element(By.NAME, "password").send_keys("admin123")
        # self.driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-tab").click()
        # self.driver.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/Yusuf/PycharmProjects/pythonProject/POMProject/report"))



