from tests.locators.register_page import RegisterPageLocators
from tests.page_model.base_page import BasePageModel


class RegisterPageModel(BasePageModel):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def title(self):
        return self.driver.find_element(*RegisterPageLocators.TITLE).text

    @property
    def url(self):
        return super(RegisterPageModel, self).url + "/register.jsp"

    @property
    def username(self):
        return self.driver.find_element(*RegisterPageLocators.USERNAME)

    @property
    def password1(self):
        return self.driver.find_element(*RegisterPageLocators.PASSWORD1)

    @property
    def password2(self):
        return self.driver.find_element(*RegisterPageLocators.PASSWORD2)

    @property
    def register_button(self):
        return  self.driver.find_element(*RegisterPageLocators.REGISTER_BUTTON)