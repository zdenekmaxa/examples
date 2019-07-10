def adder1(a):
    def wrapper(b):
        return a+b
    return wrapper


def adder2(a):
    s = a

    def wrapper(b):
        return s+b
    return wrapper


def test_adder_1():
    a = adder1(10)
    assert a(5) == 15


def test_adder_2():
    assert adder2(20)(10) == 30
