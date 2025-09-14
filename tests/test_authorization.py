import pytest
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"), # both fields are filled wit wrong values
        ("  ", "password"),                  # empty email field
        ("user.name@gmail.com", "  "),       # empty password field
    ],
    ids=[
        "invalid_both",
        "invalid_email_only",
        "invalid_password_only",
],
)

# Using fixture 'chromium_page', ready to use page которая автоматически предоставляет готовую страницу
def test_wrong_email_or_password_authorization(
        login_page: LoginPage,    # replace "chromium_page: Page," - to "login_page: LoginPage," fixture
        email:str,
        password:str
):
    # Improve code with Page object
    # login_page = LoginPage(page=chromium_page), after creation fixture login page no need to Initialize LoginPage.
    # Visit login page

    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    # Fill login form using LoginFormComponent
    login_page.login_form.fill(email=email, password=password)
    # Submit the form
    login_page.click_login_button()

    # Validate error alert is shown
    login_page.check_visible_wrong_email_or_password_alert()      # ensure that we got error alert message with correct text




    # python -m pytest -s -v -k "test_wrong_email_or_password_authorization"



