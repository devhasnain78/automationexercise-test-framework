import json

import pytest
from playwright.sync_api import Playwright, Page, expect

from page_objects.login_page import LoginPage
from page_objects.products_page import ProductsPage
from page_objects.signup_page import SignUpPage

with open("data/signup_creds.json") as data:
     new = json.load(data)
     signup_data = new["sign_up_details"]
     form_data = new["form_details"]

with open("data/login_creds.json") as creds:
    details = json.load(creds)
    login_data = details["user_details"]

## TC001 – Register User
@pytest.mark.parametrize("signup_details,form_details",list(zip(signup_data, form_data)), indirect=True)
def test_register_user(browser_instance, signup_details, form_details):
    password = signup_details["user_password"]
    sign_up = SignUpPage(browser_instance)
    sign_up.navigation()
    next_form = sign_up.sign_up(signup_details)
    next_form.next_form(password, form_details)

## TC002 - Login with valid credentials
@pytest.mark.parametrize("login_details", login_data)
def test_user_login(page:Page,browser_instance, login_details):
    email = login_details["user_mail"]
    password = login_details["user_password"]
    login = LoginPage(browser_instance)
    login.navigation()
    login.login_user(email, password)

## TC003 - Verify Products and product detail page
def test_products(browser_instance):
    produs = ProductsPage(browser_instance)
    produs.navigation()
    prod_list = produs.products_list()
    expect(prod_list).to_be_visible()
    info = produs.view_product()
    expect(info).to_be_visible()



