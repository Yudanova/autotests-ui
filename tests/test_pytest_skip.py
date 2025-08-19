import pytest

@pytest.mark.skip(reason="feature is still in progress") # Marker says: skip this test.
def test_feature_in_development():
    pass
# python -m pytest -k "test_feature_in_development" -s -v  - run this test