class AddProductPage:
    def __init__(self, page):
        self.page = page

    def navigation(self):
        self.page.goto("https://automationexercise.com/", wait_until="domcontentloaded")

    def add_product(self):
        nav = self.page.locator(".container")
        nav.get_by_role(role="link", name="Products").click()
        items = self.page.locator(".single-products")
        item_1 = items.nth(0)
        item_1.hover()
        item_1.locator(".product-overlay .add-to-cart").click()


