from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # trying to check non existent locator on the page
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    # Trying to put text into the Login button
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    # Try to change Title text
    page.evaluate("""
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = 'New Text';
        """)

    # to resolve it, add explicit wait for page to load
    # page.goto(
    #     "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
    #     wait_until='networkidle'  # waiting for network requests on the page to complete (all DOM elements)
    # )
