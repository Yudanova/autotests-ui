from playwright.sync_api import Page   # Import class Page

class BasePage:
    # Class Constructor init accepts Page object, принимающий объект Page
    def __init__(self, page: Page):
        self.page = page  # Assign the Page object to the class attribute Присваиваем объект page атрибуту класса

    def visit(self, url: str):  # method to open links
        self.page.goto(url, wait_until='networkidle')  #wait for completely page requests loading

    def reload(self):  # method reload a page 
        self.page.reload(wait_until='domcontentloaded')
