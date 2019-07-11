"""
the default named argument is evaluated only once and all subsequent calls share the
previous instance, thus keeping the previous state.

https://docs.python-guide.org/writing/gotchas/

"""


def append_to(element, to=[]):
    to.append(element)
    return to


def append_to_not_modified(_, to=[]):
    return to


def test_default_argument():
    assert append_to(12) == [12]
    assert append_to(42) == [12, 42]
    # a new instance is provided
    assert append_to(43, to=[44]) == [44, 43]
    # previously existing instance of to is revived
    assert append_to(45) == [12, 42, 45]


def test_default_argument_not_modified():
    r1 = append_to_not_modified(1)
    assert r1 == []
    assert append_to_not_modified(1, to=[2, 3]) == [2, 3]
    r2 = append_to_not_modified(1)
    assert r2 == []
    assert r1 == r2
    # more over, it's the same list that was created in the first call
    assert r1 is r2


def test_default_argument_not_modified_the_other_order():
    assert append_to_not_modified(1, to=[2, 3]) == [2, 3]
    r1 = append_to_not_modified(1)
    assert r1 == []
