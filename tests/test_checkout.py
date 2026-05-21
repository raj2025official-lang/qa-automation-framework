from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_checkout_flow(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    inventory.add_item_to_cart()

    driver.implicitly_wait(5)

    inventory.go_to_cart()

    assert "cart" in driver.current_url.lower(), f"Current URL: {driver.current_url}"