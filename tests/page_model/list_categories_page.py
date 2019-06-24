from tests.locators.list_categories_page import ListCategoriesPageLocators
from tests.page_model.base_page import BasePageModel


class ListCategoriesPageModel(BasePageModel):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def url(self):
        return super(ListCategoriesPageModel, self).url + "/listcategories.jsp"

    @property
    def title(self):
        return self.driver.find_element(*ListCategoriesPageLocators.TITLE)

    @property
    def add_category_link(self):
        return self.driver.find_element(*ListCategoriesPageLocators.ADD_CATEGORY_LINK)

    @property
    def edit_category(self):
        return self.driver.find_element(*ListCategoriesPageLocators.EDIT_CATEGORY)

    @property
    def delete_category(self):
        return self.driver.find_element(*ListCategoriesPageLocators.DELETE_CATEGORY)

    def go_to_list_categories_page(self):
        self.driver.get(self.url)
