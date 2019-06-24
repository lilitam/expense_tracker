from selenium.webdriver.common.by import By


class ListCategoriesPageLocators:
    TITLE = By.TAG_NAME, 'h1'
    ADD_CATEGORY_LINK = By.ID, 'go_add_category'
    All_CATEGORIES = By.CSS_SELECTOR, 'body > div > table > tbody > tr > td:nth-child(1)'
    EDIT_CATEGORY = By.CSS_SELECTOR, 'td:nth-child(2) > a[id^="edit"]'
    DELETE_CATEGORY = By.CSS_SELECTOR, 'td:nth-child(2) > a[id^="delete"]'
