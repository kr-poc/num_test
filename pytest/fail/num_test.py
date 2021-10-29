def inc(x):
    return x + 1


def test_fail1():
    assert inc(3) == 5

def test_fail2():
    assert inc(4) == 6
