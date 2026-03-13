import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def signup_details(request):
    return request.param
@pytest.fixture
def form_details(request):
    return request.param

@pytest.fixture
def login_details(request):
    return request.param

@pytest.fixture
def products(request):
    return request.param
@pytest.fixture
def browser_instance(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    cntxt = browser.new_context()
    page = cntxt.new_page()
    yield page
    cntxt.close()
    browser.close()