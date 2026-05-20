from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory"))
        )
        button.click()

    def add_all_items(self):
        items = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "btn_inventory"))
        )

        for item in items:
            item.click()

    def go_to_cart(self):
        cart = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart.click()

    def remove_item_from_cart(self):
        remove_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
        )
        remove_btn.click()