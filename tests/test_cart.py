import pytest

# from pages.home_page import HomePage
from utilities.file_reader import read_csv
from playwright.sync_api import Page


def test_navigate_to_cart(page:Page, home_page, cart_page) -> None:
    home_page.open()
    # login_page = home_page.go_to_login()
    cart_page.navigate_to_cart()
    cart_page.click_cart_items_link()
    # cart_page.click_product_overlay()
    cart_page.click_add_to_cart()
    cart_page.click_view_cart_link()
