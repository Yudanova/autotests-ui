from playwright. sync_api import sync_playwright , expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill("user.name@gmail.com")
    expect(registration_email_input).to_be_visible()

    registration_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    registration_name_input.fill("username")
    expect(registration_name_input).to_be_visible()

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill("password")
    expect(registration_password_input).to_be_visible()

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_visible()
    registration_button.click()


    dashboard_title = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_title).to_have_text("Dashboard")
    #expect(page).to_have_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")
    #expect(page.get_by_test_id("dashboard-toolbar-title-text")).to_have_text("Dashboard", timeout=10000)
    #expect(page.get_by_test_id("dashboard-toolbar-title-text")).to_have_text("Dashboard")



    page.wait_for_timeout(10000)