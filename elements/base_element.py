from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page:Page, locator: str, name:str):
        self.page = page
        self.locator = locator
        self.name = name

    def get_locator(self, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator)

    def click(self, **kwargs):
        # "Lazily" initialize the locator
        locator = self.get_locator(**kwargs)
        # Click on the element
        locator.click()

    def check_visible(self, **kwargs):
        # initialize the locator
        locator = self.get_locator(**kwargs)
        # Check element to be visible
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_have_text(text)