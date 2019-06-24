from selenium.webdriver.common.by import By


class RegisterPageLocators:
    TITLE = By.TAG_NAME, 'h3'
    USERNAME = By.ID, 'login'
    PASSWORD1 = By.ID, 'password1'
    PASSWORD2 = By.ID, 'password2'
    REGISTER_BUTTON = By.ID, 'submit'
    RESET_BUTTON = By.ID, 'reset'
