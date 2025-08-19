import pytest

# @pytest.mark.registration
# def test_user_registration():
#     pass
#
# @pytest.mark.smoke
# def test_user_login():
#     pass
#
# @pytest.mark.registration
# @pytest.mark.regression
# def test_password_reset():
#   pass

# python -m pytest -m "
# registration" -s -v; python -m pytest -m "registration"

# @pytest.mark.slow
# def test_heavy_calculation():
#     pass
#
#
# @pytest.mark.integration
# def test_integration_with_external_api():
#     pass
#
#
# @pytest.mark.smoke
# def test_quick_check():
#     pass

# python -m pytest -m "not slow and not integration"  - only test_quick_check should be run


# @pytest.mark.performance
# def test_memory_usage():
#     pass
#
# @pytest.mark.slow
# class TestStress:
#     def test_stress_1(self):
#         pass
#
#     @pytest.mark.performance
#     def test_stress_2(self):
#         pass
# # python -m pytest -m "not slow" - for only test_memory_usage



@pytest.mark.smoke
def test_user_exists():
    pass


# @pytest.mark.regression
# class TestUserFlow:
#     @pytest.mark.smoke
#     def test_user_can_login(self):
#         pass
#
#     def test_user_can_register(self):
#         pass
#
# @pytest.mark.feature_x
# class TestFeatureX:
#     @pytest.mark.smoke
#     def test_feature_x_works(self):
#         pass

    # python -m pytest -m "smoke and regression"  - for class TestUserFlow + smoke only

    @pytest.mark.smoke
    class TestLogin:
        @pytest.mark.smoke
        def test_valid_login(self):
            pass

        @pytest.mark.regression
        def test_invalid_login(self):
            pass

    @pytest.mark.regression
    class TestRegistration:
        @pytest.mark.regression
        def test_valid_registration(self):
            pass

        @pytest.mark.smoke
        def test_invalid_registration(self):
            pass

    @pytest.mark.smoke
    @pytest.mark.regression
    class TestCheckout:
        @pytest.mark.smoke
        @pytest.mark.regression
        def test_valid_checkout(self):
            pass

        def test_invalid_checkout(self):
            pass

    def test_search():
        pass

    # python -m pytest -m "smoke or regression"