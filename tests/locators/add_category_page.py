from selenium.webdriver.common.by import By

class AddCategoryPageLocators:
    TITLE = By.TAG_NAME, 'h1'
    NEW_CATEGORY_NAME = By.ID, 'name'
    CREATE_CATEGORY_BUTTON = By.ID, 'submit'
    RESET_BUTTON = By.ID, 'reset'
