from tests.locators.add_category_page import AddCategoryPageLocators
from tests.page_model.base_page import BasePageModel


class AddCategoryPageModel(BasePageModel):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def url(self):
        return super(AddCategoryPageModel, self).url + "/addcategory.jsp"

    @property
    def title(self):
        return self.driver.find_element(*AddCategoryPageLocators.TITLE)

    @property
    def new_category_name(self):
        return self.driver.find_element(*AddCategoryPageLocators.NEW_CATEGORY_NAME)

    @property
    def create_category_button(self):
        return self.driver.find_element(*AddCategoryPageLocators.CREATE_CATEGORY_BUTTON)

    @property
    def reset_button(self):
        return self.driver.find_element(*AddCategoryPageLocators.RESET_BUTTON)