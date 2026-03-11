class SignupForm:
    def __init__(self, page):
        self.page = page

    def next_form(self, password, form_details):
        self.page.get_by_role("radio", name="Mr.").click()
        self.page.locator("#password").fill(password)
        self.page.locator("#days").select_option("14")
        self.page.locator("#months").select_option("January")
        self.page.locator("#years").select_option("1997")
        self.page.get_by_role("checkbox", name="newsletter").check()
        self.page.locator("#optin").check()

        for field, value in form_details.items():
            self.page.locator(f"#{field}").fill(value)

        self.page.get_by_role(role="button", name="Create Account").click()
