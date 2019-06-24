from selenium.webdriver.common.by import By


class LoginPageLocators:
    TITLE = By.TAG_NAME, 'h3'
    USERNAME = By.ID, 'login'
    PASSWORD = By.ID, 'password'
    LOGIN_BUTTON = By.ID, 'submit'
    RESET_BUTTON = By.ID, 'reset'
    LINK_TO_REGISTER_PAGE = By.LINK_TEXT, "Register new user"

