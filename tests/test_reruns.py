import random
import pytest

PLATFORM = "Linux" #"Windows"   #"Linux"


@pytest.mark.flaky(reruns=3, reruns_delay=2)  # Rerun with marker flaky.
# Where: reruns=3 — amount of reruns, if test will fail it will be rerun 3 times; reruns_delay=2 - Delay between reruns in seconds
def test_reruns():
    assert random.choice([True, False])  # Random choice for unstable test, случайным образом выбирает True или False as a result, что создаёт нестабильное поведение теста.
    # assert False


@pytest.mark.flaky(reruns=3, reruns_delay=2)  # Test class
class TestReruns:
    def test_rerun_1(self):
        assert random.choice([True, False])

    def test_rerun_2(self):
        assert random.choice([True, False])



    @pytest.mark.flaky(reruns=3, reruns_delay=2, condition=PLATFORM == "Linux")  # With condition - see cons - "PLATFORM" / Перезапуск при выполнении условия
    def test_rerun_with_condition():
        assert random.choice([True, False])





# python -m pytest -k "test_reruns" -s -v
# python -m pytest -k "test_rerun_with_condition" -s -v


