from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_price_validation(driver):

    # Step 1: Open website
    driver.get("https://www.saucedemo.com/")

    # Step 2: Login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # Step 3: Add product
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()

    # Step 4: Go to cart
    inventory.go_to_cart()

    # Step 5: Get prices
    cart = CartPage(driver)
    prices = cart.get_prices()

    # Step 6: Validate prices exist
    assert len(prices) > 0, "No prices found in cart!"

    # Step 7: Validate prices are float
    for price in prices:
        assert isinstance(price, float), f"Invalid price format: {price}"

    # Step 8: Validate total
    total = sum(prices)

    print("Total Cart Price:", total)

    assert total > 0, "Total price should be greater than 0"