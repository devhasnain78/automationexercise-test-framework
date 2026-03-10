import json

import pytest
from playwright.sync_api import Playwright

from page_objects.signup_page import SignUpPage

with open("data/creds.json") as data:
     new = json.load(data)
     data = new["sign_up_details"]

@pytest.mark.parametrize('sign_up_details', data)
def test_main(playwright:Playwright, browser_instance, sign_up_details):
    name = sign_up_details["user_name"]
    email = sign_up_details["user_email"]
    sign_up = SignUpPage(browser_instance)
    sign_up.navigation()
    sign_up.sign_up(name, email)
