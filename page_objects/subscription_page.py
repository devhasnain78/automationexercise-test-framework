class SubscriptionPage:
    def __init__(self, page):
        self.page = page
    def navigation(self):
        self.page.goto("https://automationexercise.com/", wait_until="domcontentloaded")

    def verify_subscription(self, email):
        footer = self.page.locator("#footer")
        footer.scroll_into_view_if_needed()
        footer.locator("#susbscribe_email").fill(email)
        footer.locator("#subscribe").click()

    def sucess_alert(self):
        return self.page.locator(".alert-success")


