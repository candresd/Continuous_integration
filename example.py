

def add(a, b):
    return a + b


def test_add():
    assert abs(add(0.1, 0.2) - 0.3)<1e-6
