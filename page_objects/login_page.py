class LoginPage:
    def __init__(self,page):
        self.page = page

    def navigation(self):
        self.page.goto("https://automationexercise.com/", wait_until="domcontentloaded")

    def login_user(self, email, password):
        self.page.get_by_role(role="link", name=" Signup / Login").click()
        self.page.locator('[data-qa="login-email"]').fill(email)
        self.page.get_by_placeholder("Password").fill(password)
        self.page.get_by_role(role="button", name="Login").click()
