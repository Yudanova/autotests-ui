from playwright.sync_api import expect
from elements.base_element import BaseElement

class Button(BaseElement):
    def check_enabled(self, **kwargs):
        locator = self.get_locator(**kwargs)
        expect(locator).to_be_visible()
        

