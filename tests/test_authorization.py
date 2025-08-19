import pytest
from playwright.sync_api import sync_playwright, expect, Page

@pytest.mark.regression
@pytest.mark.authorization
# Использование фикстуры 'chromium_page', которая автоматически предоставляет готовую страницу
def test_wrong_email_or_password_authorization(chromium_page: Page):
    # Теперь страница передаётся в тест через фикстуру 'chromium_page', браузер не нужно инициализировать вручную
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill("user.name@gmail.com")

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill("password")

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

    # python -m pytest -m "authorization or registration" -s -v


# def test_wrong_email_or_password_authorization():  # Create test function, covering previous playwright's script by "def"
#
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         page = browser.new_page()
#
#         page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
#
#         email_input = page.get_by_test_id('login-form-email-input').locator('input')
#         email_input.fill("user.name@gmail.com")
#
#         password_input = page.get_by_test_id('login-form-password-input').locator('input')
#         password_input.fill("password")
#
#         login_button = page.get_by_test_id('login-page-login-button')
#         login_button.click()
#
#         wrong_email_or_password_alert = page.get_by_test_id('login-page-wrong-email-or-password-alert')
#         expect(wrong_email_or_password_alert).to_be_visible()
#         expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")

# Основные изменения:
#
# Удалена ручная инициализация браузера: Теперь не нужно использовать sync_playwright() и вручную создавать браузер и страницу, это делает фикстура chromium_page.
# Фикстура chromium_page в параметрах теста: Тест принимает параметр chromium_page: Page, который автоматически предоставляет страницу, созданную через фикстуру.
# Таким образом, фикстура chromium_page позволяет переиспользовать инициализацию Playwright в тестах, что делает код чище и удобнее для поддержки.

        # "wait for timeout" was removed / убрали sleep
        # python -m pytest -m authorization -s -v