import pytest  # Импортируем pytest
from playwright.sync_api import sync_playwright, Page, Playwright
     # Имопртируем класс страницы, будем использовать его для аннотации типов


# @pytest.fixture  # Declare fixture, scope function by default (what we need)
# def chromium_page() -> Page:  # Аннотируем возвращаемое фикстурой значение
#     # Ниже идет инициализация и открытие новой страницы
#     with sync_playwright() as playwright:
#         # Запускаем браузер
#         browser = playwright.chromium.launch(headless=False)
#
#         # Передаем страницу для использования в тесте
#         yield browser.new_page()
#
#         # Закрываем браузер после выполнения тестов
#         browser.close()

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
        browser = playwright.chromium.launch(headless=False)
        yield browser.new_page()
        browser.close()