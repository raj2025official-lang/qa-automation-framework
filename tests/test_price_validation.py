import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def driver():

    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()


def test_price_validation(driver):

    # Step 1: Open website
    driver.get("https://www.saucedemo.com/")

    # Step 2: Login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # Step 3: Add product(s)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()

    # Step 4: Go to cart
    inventory.go_to_cart()

    # Step 5: Get prices from cart
    cart = CartPage(driver)
    prices = cart.get_prices()

    # Step 6: Validation
    assert len(prices) > 0, "No prices found in cart!"

    # Step 7: Check all prices are valid numbers
    for price in prices:
        assert isinstance(price, float), f"Invalid price format: {price}"

    # Step 8: Optional total check
    total = sum(prices)
    print("Total Cart Price:", total)

    assert total > 0, "Total price should be greater than 0"