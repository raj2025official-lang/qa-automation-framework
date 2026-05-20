from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_remove_item(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    inventory.add_item_to_cart()

    driver.implicitly_wait(5)

    inventory.remove_item_from_cart()

    assert True