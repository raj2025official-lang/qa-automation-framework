from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    # Remove item
    def remove_item(self):
        remove_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
        )
        remove_button.click()

    # Checkout
    def checkout(self):
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

    # Get all cart items
    def get_items(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    # Get all prices
    def get_prices(self):
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")

        price_list = []

        for price in prices:
            value = price.text.replace("$", "")
            price_list.append(float(value))

        return price_list

    # Check item exists in cart
    def is_item_in_cart(self):
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return len(items) > 0