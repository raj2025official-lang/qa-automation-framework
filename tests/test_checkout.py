from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_checkout_flow(driver):

    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)

    # checkout
    cart.checkout()

    assert "checkout-step-one" in driver.current_url