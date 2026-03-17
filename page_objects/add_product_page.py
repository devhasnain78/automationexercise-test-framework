class AddProductPage:
    def __init__(self, page):
        self.page = page

    def navigation(self):
        self.page.goto("https://automationexercise.com/", wait_until="domcontentloaded")

    def add_product(self):
        nav = self.page.locator(".container")
        nav.get_by_role(role="link", name="Products").click()
        items = self.page.locator(".single-products")

        for i in range(2):
            item = items.nth(i)
            item.scroll_into_view_if_needed()
            item.hover()
            btn = item.locator(".product-overlay .add-to-cart")
            btn.wait_for(state="visible")
            btn.click()
            modal = self.page.locator(".modal-content")
            modal.get_by_role(role="button", name="Continue Shopping").click()
