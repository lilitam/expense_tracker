from tests.locators.login_page import LoginPageLocators
from tests.page_model.base_page import BasePageModel


class LoginPageModel(BasePageModel):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def title(self):
        return self.driver.find_element(*LoginPageLocators.TITLE).text

    @property
    def url(self):
        return super(LoginPageModel, self).url + "/index.jsp"

    @property
    def username(self):
        return self.driver.find_element(*LoginPageLocators.USERNAME)

    @property
    def password(self):
        return self.driver.find_element(*LoginPageLocators.PASSWORD)

    @property
    def login_button(self):
        return  self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

    @property
    def link_to_register_page(self):
        return self.driver.find_element(*LoginPageLocators.LINK_TO_REGISTER_PAGE)



