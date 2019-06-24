from tests.locators.edit_expense_page import EditExpensePageLocators
from tests.page_model.base_page import BasePageModel


class EditExpensePageModel(BasePageModel):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def day(self):
        return self.driver.find_element(*EditExpensePageLocators.DAY)

    @property
    def month(self):
        return self.driver.find_element(*EditExpensePageLocators.MONTH)

    @property
    def year(self):
        return self.driver.find_element(*EditExpensePageLocators.YEAR)

    @property
    def category(self):
        return self.driver.find_element(*EditExpensePageLocators.CATEGORY)

    @property
    def amount(self):
        return self.driver.find_element(*EditExpensePageLocators.AMOUNT)

    @property
    def reason(self):
        return self.driver.find_element(*EditExpensePageLocators.REASON)

    @property
    def save_expense_button(self):
        return self.driver.find_element(*EditExpensePageLocators.SAVE_EXPENSE_BUTTON)

    @property
    def reset_button(self):
        return self.driver.find_element(*EditExpensePageLocators.RESET_BUTTON)
