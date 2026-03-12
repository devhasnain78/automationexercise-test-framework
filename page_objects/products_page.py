
class ProductsPage:
    def __init__(self, page):
        self.page = page

    def navigation(self):
        self.page.goto("https://automationexercise.com/", wait_until="domcontentloaded")

    def products_list(self):
        self.page.get_by_role(role="link", name="Products").click()
        return self.page.locator(".features_items")

    def view_product(self):
        card = self.page.locator(".product-image-wrapper").nth(0)
        card.get_by_role(role="link", name="View Product").click()
        info = self.page.locator(".product-information")
        return info


