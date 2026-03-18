class AddProductPage:
    def __init__(self, page):
        self.page = page

    def navigation(self):
        self.page.goto("https://automationexercise.com/", wait_until="domcontentloaded")

    def add_product(self):
        self.selected_products = []
        nav = self.page.locator(".container")
        nav.get_by_role(role="link", name="Products").click()

        for i in range(2):
            items = self.page.locator(".single-products")
            item = items.nth(i)
            item.scroll_into_view_if_needed()
            item.hover()
            price = item.locator(".product-overlay h2").text_content()
            self.selected_products.append(price)
            btn = item.locator(".product-overlay .add-to-cart")
            btn.wait_for(state="visible")
            btn.click()
            modal = self.page.locator(".modal-content")
            if i==0:
                modal.get_by_role(role="button", name="Continue Shopping").click()
            else:
                modal.get_by_role(role="link", name="View Cart").click()
            return self.selected_products

    def view_cart(self):
        self.page.goto("https://automationexercise.com/view_cart")
        cart = self.page.locator(".cart_price p").all_text_contents()
        return cart

