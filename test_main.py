import json

import pytest
from playwright.sync_api import Playwright, Page

from page_objects.signup_page import SignUpPage

with open("data/creds.json") as data:
     new = json.load(data)
     signup_data = new["sign_up_details"]
     form_data = new["form_details"]

@pytest.mark.parametrize("signup_details,form_details",list(zip(signup_data, form_data)), indirect=True)
def test_main(browser_instance, signup_details, form_details):
    password = signup_details["user_password"]
    sign_up = SignUpPage(browser_instance)
    sign_up.navigation()
    next_form = sign_up.sign_up(signup_details)
    next_form.next_form(password, form_details)

