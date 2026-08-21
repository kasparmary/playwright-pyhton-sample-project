from __future__ import annotations

from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.cart_link = page.get_by_role("link", name="Cart")
        self.view_full_cart_items = page.get_by_role("link", name="here")
        # self.add_tocart = page.get_by_text("Add to cart").nth(1)
        # self.product_overlay = page.locator(".product-overlay")
        self.view_cart_link = page.get_by_role("link", name="View Cart")

        self.product = page.locator(".product-image-wrapper").filter(has_text="Blue Top")
        self.product_sub = self.product.locator("a.add-to-cart")

    def navigate_to_cart(self) -> None:
        self.cart_link.click()

    def click_cart_items_link(self) -> None:
        self.view_full_cart_items.click()

    # def click_product_overlay(self) -> None:
    #     self.product_overlay.first.hover()

    def click_add_to_cart(self) -> None:
        # self.add_cart.hover()
        # self.add_tocart.click()
        self.product_sub.first.click()

    def click_view_cart_link(self) -> None:
        self.view_cart_link.click()
