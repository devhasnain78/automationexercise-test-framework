import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def sign_up_details(request):
    return request.params

@pytest.fixture
def browser_instance(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    cntxt = browser.new_context()
    page = cntxt.new_page()
    yield page
    cntxt.close()
    browser.close()