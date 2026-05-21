from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_checkout_flow(driver):

    # Open website
    driver.get("https://www.saucedemo.com/")

    # Login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # Add product
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()

    # Go to cart
    inventory.go_to_cart()

    # Validation
    current_url = driver.current_url.lower()

    assert "cart" in current_url, f"Failed! Current URL is: {current_url}"

    print("Checkout navigation successful!")