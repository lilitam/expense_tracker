from random import random
from unittest import TestCase
from selenium import webdriver

from tests.system.helpers.category import Category
from tests.system.helpers.register import Register


class ListCategories(TestCase):
    def setUp(self):
        # registering new user for each test case
        self.driver = webdriver.Chrome()
        self.register = Register(self.driver)
        self.register.go_to_register_page()
        self.register.register_user('test' + str(random()), 1234)

    def test_add_new_category(self):
        # verifying that new created category name is shown on 'list categories' page
        category = Category(self.driver)
        category.add('home')
        new_category = category.find_category_by_name('home')

        self.assertIsNotNone(new_category, "Cannot find category with name 'home' in 'List Categories' page")

    def test_edit_category_name(self):
        category = Category(self.driver)
        category.add('home')
        category.rename('home', 'lunch')

        # verifying that on 'list categories' page, category name is updated from 'home' to 'lunch'
        self.assertIsNotNone(category.find_category_by_name('lunch'))
        self.assertIsNone(category.find_category_by_name('home'))

    def test_delete_unused_category(self):
        category = Category(self.driver)
        category.add('home')
        category.add('lunch')

        category.delete('home')

        # verifying that the deleted category name is not shown on 'List Categories' page
        self.assertIsNone(category.find_category_by_name('home'))
        self.assertIsNotNone(category.find_category_by_name('lunch'))

    def tearDown(self):
        self.driver.quit()


