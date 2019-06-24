from random import random

from selenium import webdriver
from unittest import TestCase

from tests.page_model.list_expenses_page import ListExpansesPageModel
from tests.system.helpers.register import Register


class RegisterPage(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_successful_registration(self):
        register_page = Register(self.driver)
        register_page.go_to_register_page()
        register_page.register_user('test' + str(random()), 1234)
        list_expenses_page = ListExpansesPageModel(self.driver)
        self.assertEqual(self.driver.current_url, list_expenses_page.url)
        self.assertIn(list_expenses_page.title, self.driver.page_source)

    # Test if the registration fails with incorrect username format
    # username - at least 4 characters
    def test_username_incorrect_format(self):
        register_page = Register(self.driver)
        register_page.go_to_register_page()
        register_page.register_user('abc', 1234)

        page_model = register_page.get_page_model()
        self.assertEqual(page_model.username.get_attribute("validationMessage"), 'Please match the requested format.')
        self.assertEqual(page_model.username.get_attribute("title"), 'username - at least 4 characters')

    def test_incorrect_password_confirmation(self):
        register_page = Register(self.driver)
        register_page.go_to_register_page()
        register_page.register_user('test' + str(random()), 1234, 5678)

        self.assertEqual(self.driver.switch_to.alert.text, "Error: Passwords aren't equal!")
        self.driver.switch_to.alert.accept()

    def tearDown(self):
        self.driver.quit()
