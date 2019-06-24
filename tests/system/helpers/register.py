from selenium.webdriver.support.wait import WebDriverWait

from tests.page_model.base_page import BasePageModel
from tests.page_model.register_page import RegisterPageModel


class Register(BasePageModel):
    def __init__(self, driver):
        self.driver = driver
        self.register_page_model = RegisterPageModel(self.driver)

    def register_user(self, username=False, password1=False, password2=False):
        if password2:
            password2 = password2
        else:
            password2 = password1

        # register_user user
        self.register_page_model.username.send_keys(username)
        self.register_page_model.password1.send_keys(password1)
        self.register_page_model.password2.send_keys(password2)
        self.register_page_model.register_button.click()

    def logout(self):
        # logout the user
        logout = WebDriverWait(self.driver, 5).until(lambda driver: driver.find_element_by_id('logout'))
        logout.click()

    def get_page_model(self):
        return self.register_page_model

    def go_to_register_page(self):
        self.driver.get(super(Register, self).url + '/register.jsp')
