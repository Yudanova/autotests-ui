import pytest

from playwright.sync_api import sync_playwright, expect, Page

from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage



@pytest.mark.courses
@pytest.mark.regression
@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    page = CoursesListPage(chromium_page_with_state)
    page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Checking components
    page.check_visible_navbar()
    page.check_visible_sidebar()

    # Checking Page's elements
    page.check_visible_courses_title()
    page.check_visible_create_course_button()
    page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view(is_image_uploaded=False)
    create_course_page.check_visible_create_course_form(
        title="", max_score="0", min_score="0", description="", estimated_time=""
    )

    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()

    create_course_page.upload_preview_image("./testdata/files/image.jpg")
    create_course_page.check_visible_image_upload_view(is_image_uploaded=True)
    create_course_page.fill_create_course_form(
        title="Playwright",
        max_score="100",
        min_score="10",
        description="Playwright",
        estimated_time="2 weeks"
    )
    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0, title="Playwright", max_score="100", min_score="10", estimated_time="2 weeks"
    )

    print(dir(create_course_page))
    print(create_course_page.__class__)

# def test_empty_courses_list(): # Create test function
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()

# page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")
# registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
# registration_email_input.fill("user.name@gmail.com")
#
# registration_name_input = page.get_by_test_id('registration-form-username-input').locator('input')
# registration_name_input.fill("username")
#
# registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
# registration_password_input.fill("password")
#
# registration_button = page.get_by_test_id('registration-page-registration-button')
# registration_button.click()
#
# context.storage_state(path="browser-state.json")

# with sync_playwright() as playwright:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context(storage_state="browser-state.json")
#     page = context.new_page()
#     # page = browser.new_page()


# page.wait_for_timeout(5000)
# python -m pytest -v -s -k "test_empty_courses_list"
# python -m pytest -v -s -k  "test_create_course"
# python -m pytest -k "test_empty_courses_list" -s -v
