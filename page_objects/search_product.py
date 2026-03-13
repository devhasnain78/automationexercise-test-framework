class SearchProduct:
    def __init__(self, page):
        self.page = page

    def navigation(self):
        self.page.goto("https://automationexercise.com/", wait_until="domcontentloaded")

    def search_product(self, prod_name):
        self.page.get_by_role(role="link", name="Products").click()
        self.page.get_by_placeholder("Search Product").fill(prod_name["name"])
        self.page.locator("#submit_search").click()

    def after_search(self, prod_name):
        return self.page.locator(".features_items").get_by_text(prod_name['name']).first