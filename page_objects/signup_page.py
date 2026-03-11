from page_objects.signup_form import SignupForm


class SignUpPage:
    def __init__(self, page):
        self.page = page
    def navigation(self):
        self.page.goto("https://automationexercise.com/", wait_until="domcontentloaded")

    def sign_up(self, signup_details):
        name = signup_details["user_name"]
        email = signup_details["user_email"]
        self.page.get_by_role(role="link", name=" Signup / Login").click()
        self.page.get_by_placeholder("Name").fill(name)
        self.page.locator('[data-qa="signup-email"]').fill(email)
        self.page.get_by_role(role="button", name="Signup").click()

        signup_form = SignupForm(self.page)
        return signup_form

