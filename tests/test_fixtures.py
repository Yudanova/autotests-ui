import pytest


# Function that will be automatically called for each test
@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Send data to the analytical service")


# Fixture for initialization autotest's settings on the session level
@pytest.fixture(scope='session')
def settings():
    print("[SESSION] initialization autotest's settings")


# Fixture for user data creation, that will run once per class
@pytest.fixture(scope='class')
def user():
    print("[CLASS] Create user data for once per class")


# Fixture to open browser, runs for each test
@pytest.fixture(scope='function')
def browser():
    print("[FUNCTION] Open browser for each autotest")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        pass

    def test_user_can_create_course(self, settings, user, browser):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        pass

    # python -m pytest -k "TestUserFlow or TestAccountFlow" -s -v