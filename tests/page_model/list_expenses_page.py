from selenium import webdriver
from tests.locators.list_expenses_page import ListExpensesPageLocators
from tests.page_model.base_page import BasePageModel


class ListExpansesPageModel(BasePageModel):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def title(self):
        return self.driver.find_element(*ListExpensesPageLocators.TITLE).text

    @property
    def url(self):
        return super(ListExpansesPageModel, self).url + "/listexpenses"

    def go_to_list_expenses_page(self):
        self.driver.get(self.url)
