from playwright.sync_api import Page, expect
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.page = page

        # Components
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        # Page Elements
        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        self.empty_view_icon = page.get_by_test_id('courses-list-empty-view-icon')
        self.empty_view_title = page.get_by_test_id('courses-list-empty-view-title-text')
        self.empty_view_description = page.get_by_test_id('courses-list-empty-view-description-text')

    def visit(self, url: str):
        self.page.goto(url)

    def check_visible_navbar(self):
        self.navbar.check_visible("username")  # или другой ожидаемый текст

    def check_visible_sidebar(self):
        self.sidebar.check_visible()

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def check_visible_empty_view(self):
        expect(self.empty_view_icon).to_be_visible()
        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text('There is no results')
        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text(
            'Results from the load test pipeline will be displayed here'
        )