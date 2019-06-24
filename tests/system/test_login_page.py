from unittest import TestCase
from random import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.page_model.list_expenses_page import ListExpansesPageModel
from tests.system.helpers.login import LogIn
from tests.system.helpers.register import Register


class LoginPage(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_link_to_register_page(self):
        login = LogIn(self.driver)
        register = Register(self.driver)
        login_page_model = login.get_page_model()
        register_page_model = register.get_page_model()

        login.go_to_login_page()
        login_page_model.link_to_register_page.click()

        # "Go to register_user page" link should navigate to registration page
        self.assertEqual(register_page_model.url, self.driver.current_url)
        self.assertIn(register_page_model.title, self.driver.page_source)

    def test_unregistered_login(self):
        login = LogIn(self.driver)
        login.go_to_login_page()
        login.login_user("test_" + str(random()), "1234")

        wait = WebDriverWait(self.driver, 5)
        error_message = wait.until(lambda driver: driver.find_element_by_class_name('alert-danger'))

        # corresponding error message should inform when user is not registered
        self.assertEqual(error_message.text, "unknown login or wrong password")

    # Test that registered user can login successfully
    def test_successful_login(self):
        # registering new user, and testing it's successful Login
        register = Register(self.driver)
        register.go_to_register_page()
        username = "new_user" + str(random())
        password = 1234
        register.register_user(username, password)
        register.logout()

        login_user = LogIn(self.driver)
        login_user.go_to_login_page()
        login_user.login_user(username, password)

        # validating that after successful login, user is navigated to the 'list expenses' page
        list_expenses_page = ListExpansesPageModel(self.driver)
        self.assertEqual(list_expenses_page.url, self.driver.current_url)
        self.assertIn(list_expenses_page.title, self.driver.page_source)

    # Test that user with registered username and incorrect password cannot login
    def test_incorrect_password(self):
        # registering new user
        register = Register(self.driver)
        register.go_to_register_page()
        username = "new_user" + str(random())
        password = 1234
        register.register_user(username, password)
        register.logout()

        login_user = LogIn(self.driver)
        login_user.go_to_login_page()
        login_user.login_user(username, 'incorrect_password')

        # Verifying the presence of alert about incorrect password
        alert = WebDriverWait(self.driver, 5).until(
          EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        )
        self.assertEqual(alert.text, "unknown login or wrong password")

    # Test if Login fails with empty username and password
    def test_empty_credentials(self):
        login_page = LogIn(self.driver)
        login_page.go_to_login_page()
        login_page.login_user("", "")

        login_page_model = login_page.get_page_model()
        self.assertEqual(login_page_model.username.get_attribute("validationMessage"),
                         'Please fill out this field.')
        self.assertEqual(login_page_model.username.get_attribute("title"), 'username - at least 4 characters')

    def tearDown(self):
        self.driver.quit()
