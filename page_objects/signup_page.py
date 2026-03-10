class SignUpPage:
    def __init__(self, page):
        self.page = page
    def navigation(self):
        self.page.goto("https://automationexercise.com/")

    def sign_up(self, name, email):
        self.page.get_by_role(role="link", name=" Signup / Login").click()
        self.page.get_by_placeholder("Name").fill(name)
        self.page.locator('[data-qa="signup-email"]').fill(email)

