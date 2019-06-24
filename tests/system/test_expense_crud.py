from random import random

import time
from selenium import webdriver
from unittest import TestCase

from tests.page_model.add_expense_page import AddExpensePageModel
from tests.page_model.list_expenses_page import ListExpansesPageModel
from tests.system.helpers.category import Category
from tests.system.helpers.expense import Expense
from tests.system.helpers.register import Register


class AddExpensePage(TestCase):
    def setUp(self):
        # registering new user for each test case
        self.driver = webdriver.Chrome()
        self.register = Register(self.driver)
        self.register.go_to_register_page()
        self.register.register_user('test' + str(random()), 1234)
        category = Category(self.driver)
        category.add('gym')

    def test_add_expense(self):
        expense = Expense(self.driver)
        expense.add(3, 4, 2019, 'gym', 100, "sport-clothing")

        new_expense = expense.find_expense_by_date_and_category('03.04.19', 'gym')
        self.assertIsNotNone(
            new_expense, "Cannot find expense with date='03.04.19 and category_name='gym' in 'List Categories' page")

    def test_incorrect_format_amount(self):
        expense = Expense(self.driver)
        expense.add(5, 5, 2019, 'gym', 7.1004, "sport-clothing")

        add_expense_page_model = AddExpensePageModel(self.driver)
        self.assertEqual(add_expense_page_model.amount.get_attribute("validationMessage"),
                         'Please match the requested format.')
        self.assertEqual(add_expense_page_model.amount.get_attribute("title"), 'amount of expense - #0.00')

    def test_delete_expense(self):
        expense = Expense(self.driver)
        expense.add(5, 5, 2019, 'gym', 200, "sport-clothing")
        expense.delete("05.05.19", "gym")
        deleted_expense = expense.find_expense_by_date_and_category('05.05.19', 'gym')

        self.assertIsNone(deleted_expense, "Failed to delete the expense")

    def test_change_expense_category(self):
        expense = Expense(self.driver)
        list_expenses_page_model = ListExpansesPageModel(self.driver)
        category = Category(self.driver)

        expense.add(5, 5, 2019, 'gym', 200, "sport-clothing")
        category.add('home')
        list_expenses_page_model.go_to_list_expenses_page()
        expense.edit('05.05.19', 'gym', {'category': 'home'})

        changed_expense = expense.find_expense_by_date_and_category('05.05.19', 'home')
        self.assertIsNotNone(changed_expense, "Failed to change expense category")

    def tearDown(self):
        self.driver.quit()
