from playwright.sync_api import Page, expect
from components.base_component import BaseComponent


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        # Initialize the login form component
        self.email_input = page.get_by_test_id('login-form-email-input').locator('input')
        self.password_input = page.get_by_test_id('login-form-password-input').locator('input')

        # These elements are part of the page but not the form itself
        self.login_button = page.get_by_test_id('login-page-login-button')
        self.registration_link = page.get_by_test_id('login-page-registration-link')
        self.wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')

    # Fill the login form using the component
    def fill(self, email: str, password: str):
        self.email_input.fill('' if email is None else email)
        self.password_input.fill('' if password is None else password)


    # Check that the form is visible and contains the correct values
    def check_login_form_visible(self, email: str, password: str):
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        if email is not None:
            expect(self.email_input).to_have_value(email)
        if password is not None:
            expect(self.password_input).to_have_value(password)

    # Click the login button
    def click_login_button(self):
        self.login_button.click()

    # Navigate to the registration page
    def click_registration_link(self):
        self.registration_link.click()

    # Check that the "Wrong email or password" alert is visible
    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")