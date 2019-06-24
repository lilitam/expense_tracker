from selenium.webdriver.common.by import By


class EditExpensePageLocators:
    DAY = By.ID, 'day'
    MONTH = By.ID, 'month'
    YEAR = By.ID, 'year'
    CATEGORY = By.ID, 'category'
    AMOUNT = By.ID, 'amount'
    REASON = By.ID, 'reason'
    SAVE_EXPENSE_BUTTON = By.ID, 'submit'
    RESET_BUTTON = By.ID, 'reset'
