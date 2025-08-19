import pytest


# Fixture for cleaning DB
@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Remove all data from the DB")


# Fixture for filling DB
@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Create new data in DB")

@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    ...

@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...

    # python -m pytest -s -v -k "test_read_all_books_in_library or TestLibrary"