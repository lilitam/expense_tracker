from tests.locators.edit_category_page import EditCategoryPageLocators
from tests.page_model.base_page import BasePageModel


class EditCategoryPageModel(BasePageModel):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def name_field(self):
        return self.driver.find_element(*EditCategoryPageLocators.NAME)

    @property
    def save_category_button(self):
        return self.driver.find_element(*EditCategoryPageLocators.SAVE_CATEGORY_BUTTON)