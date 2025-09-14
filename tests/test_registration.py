import pytest  # library pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage



@pytest.mark.regression  # Added regression marker
@pytest.mark.registration  # Added registration marker
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):  # using fixtures

    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
# using component form
    registration_page.registration_form.fill(
        email="user.name@gmail.com",
        username="username",
        password="password"
    )
    registration_page.click_registration_button()
# user should be redirected to the dashboard page
    dashboard_page.check_visible_dashboard_title()




    # python -m pytest -s -v -k "test_successful_registration"

    # email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
    # email_input.fill('user.name@gmail.com')
    #
    # username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
    # username_input.fill('username')
    #
    # password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
    # password_input.fill('password')
    #
    # registration_button = chromium_page.get_by_test_id('registration-page-registration-button')
    # registration_button.click()
    #
    # dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
    # expect(dashboard_title).to_be_visible()

    #python -m pytest -m "authorization or registration" -s -v

# def test_successful_registration():  # Create test function
#     # This script is a copy of the same one in the "playwright_registration"
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#
#         page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')
#
#         email_input = page.get_by_test_id('registration-form-email-input').locator('input')
#         email_input.fill('user@gmail.com')
#
#         username_input = page.get_by_test_id('registration-form-username-input').locator('input')
#         username_input.fill('username')
#
#         password_input = page.get_by_test_id('registration-form-password-input').locator('input')
#         password_input.fill('password')
#
#         registration_button = page.get_by_test_id('registration-page-registration-button')
#         registration_button.click()
#
#         context.storage_state(path='browser-state.json')
#
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context(storage_state='browser-state.json')
#         page = context.new_page()
#
#         page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
#
#         page.wait_for_timeout(5000)

        # python -m pytest -m registration -s -v  run using (calling) specific marker
        # python -m pytest --markers  - show all markers (custom and imbedded markers)


        # run in terminal: python -m pytest   - a - s
        # run one, specific test in terminal: python - m pytest - v - s - k "test_successful_registration"

