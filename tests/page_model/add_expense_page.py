from tests.locators.add_expense_page import AddExpensePageLocators
from tests.page_model.base_page import BasePageModel


class AddExpensePageModel(BasePageModel):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def day(self):
        return self.driver.find_element(*AddExpensePageLocators.DAY)

    @property
    def month(self):
        return self.driver.find_element(*AddExpensePageLocators.MONTH)

    @property
    def year(self):
        return self.driver.find_element(*AddExpensePageLocators.YEAR)

    @property
    def category(self):
        return self.driver.find_element(*AddExpensePageLocators.CATEGORY)

    @property
    def amount(self):
        return self.driver.find_element(*AddExpensePageLocators.AMOUNT)

    @property
    def reason(self):
        return self.driver.find_element(*AddExpensePageLocators.REASON)

    @property
    def create_expense_button(self):
        return self.driver.find_element(*AddExpensePageLocators.CREATE_EXPENSE_BUTTON)

    @property
    def reset_button(self):
        return self.driver.find_element(*AddExpensePageLocators.RESET_BUTTON)

    def go_to_add_expense_page(self):
        self.driver.get(super(AddExpensePageModel, self).url + "/addexpense.jsp")