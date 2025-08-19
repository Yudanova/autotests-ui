import pytest

# @pytest.mark.xfail(reason="Known error, will be fixed in the next release")
# def test_known_issue():
#     pass

@pytest.mark.xfail(reason='Bug was found, it is known')
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason='Bug was fixed, but it still has marker xfail')
def test_without_bug():
    pass


@pytest.mark.xfail(reason='External service is unavailable yet')
def test_external_services_is_unavailable():
    assert 1 == 2

    # python -m pytest -k "test_with_bug or test_without_bug or test_external_services_is_unavailable" -s -v
    # #//  8 deselected, 2 xfailed, 1 xpassed in 0.31s