from selenium.webdriver.common.by import By

from tests.locators.list_categories_page import ListCategoriesPageLocators
from tests.page_model.add_category_page import AddCategoryPageModel
from tests.page_model.edit_category_page import EditCategoryPageModel
from tests.page_model.list_categories_page import ListCategoriesPageModel


class Category:
    def __init__(self, driver):
        self.driver = driver

    def add(self, name):
        # navigate to add_category page
        list_category = ListCategoriesPageModel(self.driver)
        list_category.go_to_list_categories_page()
        list_category.add_category_link.click()

        # add new category
        add_category_page = AddCategoryPageModel(self.driver)
        add_category_page.new_category_name.send_keys(name)
        add_category_page.create_category_button.click()

    def delete(self, name):
        category = self.find_category_by_name(name)
        if category:
            delete = category.parent.find_element(*ListCategoriesPageLocators.DELETE_CATEGORY)
            delete.click()
            self.driver.switch_to.alert.accept()

    def rename(self, old_name, new_name):
        category = self.find_category_by_name(old_name)
        if category:
            edit = category.parent.find_element(*ListCategoriesPageLocators.EDIT_CATEGORY)
            edit.click()
            edit_category_page = EditCategoryPageModel(self.driver)
            edit_category_page.name_field.clear()
            edit_category_page.name_field.send_keys(new_name)
            edit_category_page.save_category_button.click()

    def find_category_by_name(self, name):
        all_categories = self.driver.find_elements(*ListCategoriesPageLocators.All_CATEGORIES)
        for category in all_categories:
            if category.text == name:
                return category



