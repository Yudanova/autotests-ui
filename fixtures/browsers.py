import pytest
from playwright.sync_api import sync_playwright, expect,Page, Playwright

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()



@pytest.fixture(scope="session") # runs once per test session
def initialize_browser_state(playwright: Playwright): # Register a new user and save the browser state to a file. So you don’t have to repeat registration in every test
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")

    registration_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_name_input.fill("username")

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="browser-state.json") # No return value. It just creates browser-state.json

    browser.close()


@pytest.fixture(scope="function") # fresh page for each test
# Opens a browser page using the saved state from browser-state.json
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
        # Return a Page object you can use in your test, Returns a page with that stat
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    yield context.new_page()  # This is where Pytest pauses the fixture and passes control to my test, test runs using the page object returned by yield.

    browser.close() # Once test finishes, Pytest resumes the fixture after the yield, which is where i clean up:
