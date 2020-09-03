from my_code import times_3


def test_times_3():
    assert 15 == times_3("5")
    assert 0 == times_3("0")
    assert -3 == times_3("-1")
