from tests.page_model.base_page import BasePageModel
from tests.page_model.login_page import LoginPageModel


class LogIn(BasePageModel):
    def __init__(self, driver):
        self.driver = driver
        self.page_model = LoginPageModel(self.driver)

    def login_user(self, username=False, password=False):
        self.page_model.username.send_keys(username)
        self.page_model.password.send_keys(password)
        self.page_model.login_button.click()

    def get_page_model(self):
        return self.page_model

    def go_to_login_page(self):
        self.driver.get(super(LogIn, self).url + '/index.jsp')