from playwright.sync_api import Playwright


def test_main(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    cntxt = browser.new_context()
    page = cntxt.new_page()
    page.goto("https://automationexercise.com")