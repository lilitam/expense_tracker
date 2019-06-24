from selenium.webdriver.common.by import By

from tests.page_model.add_expense_page import AddExpensePageModel
from tests.page_model.edit_expense_page import EditExpensePageModel


class Expense:
    def __init__(self, driver):
        self.driver = driver

    def add(self, day, month, year, category, amount, reason):
        expense = AddExpensePageModel(self.driver)
        expense.go_to_add_expense_page()

        expense.day.clear()
        expense.day.send_keys(day)

        expense.month.clear()
        expense.month.send_keys(month)

        expense.year.clear()
        expense.year.send_keys(year)

        category_to_select = self.driver.find_element_by_xpath(
            "//select[@id='category']/option[text()='" + category + "']")
        category_to_select.click()

        expense.amount.clear()
        expense.amount.send_keys(str(amount))

        expense.reason.clear()
        expense.reason.send_keys(reason)

        expense.create_expense_button.click()

    def delete(self, date, category_name):
        expense = self.find_expense_by_date_and_category(date, category_name)
        if expense:
            delete = expense.find_element(By.CSS_SELECTOR, 'td:nth-child(5) > a[id^="delete"]')
            delete.click()
            self.driver.switch_to.alert.accept()

    def edit(self, old_date, old_category_name, new_data):
        day = new_data.get('day', False)
        month = new_data.get('month', False)
        year = new_data.get('year', False)
        category = new_data.get('category', False)
        amount = new_data.get('amount', False)
        reason = new_data.get('reason', False)

        expense = self.find_expense_by_date_and_category(old_date, old_category_name)
        if expense:
            edit = expense.find_element(By.CSS_SELECTOR, 'td:nth-child(5) > a[id^="edit"]')
            edit.click()

        edit_page = EditExpensePageModel(self.driver)
        if day:
            edit_page.day.send_keys(day)
        if month:
            edit_page.month.send_keys(month)
        if year:
            edit_page.year.send_keys(year)
        if amount:
            edit_page.amount.send_keys(amount)
        if reason:
            edit_page.reason.send_keys(reason)
        if category:
            category_to_select = self.driver.find_element_by_xpath(
                "//select[@id='category']/option[text()='" + category + "']")
            category_to_select.click()

        edit_page.save_expense_button.click()

    def find_expense_by_date_and_category(self, date, category_name):
        all_expenses = self.driver.find_elements(By.CSS_SELECTOR, 'body > div > table > tbody > tr')
        for expense in all_expenses:
            if expense.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text == date and \
                    expense.find_element(By.CSS_SELECTOR, 'td:nth-child(2)').text == category_name:
                return expense


