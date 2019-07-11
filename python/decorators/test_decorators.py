"""
Python decorator examples, experiments.

https://www.datacamp.com/community/tutorials/decorators-python

"""

from decorator import decorator

import pytest


def uppercase_decorator(func):
    """
    using decorator without Python decorator syntax (@ sign)

    """
    def wrapper(arg):
        """
        for general purpose, the signature would be *args, **kwargs

        """
        uppercase = func(arg).upper()
        return uppercase
    return wrapper


def repeater_without_decorator_syntax(arg):
    return arg


@uppercase_decorator
def repeater(arg):
    return arg


def test_repeater():
    # using decorator without Python decorator syntax(@ sign)
    assert uppercase_decorator(repeater_without_decorator_syntax)("hello there") == "HELLO THERE"
    assert repeater("hey hey") == "HEY HEY"


def memoize(func):
    cache = {}

    def wrapper(n):
        try:
            return cache[n]
        except KeyError:
            r = func(n)
            cache[n] = r
            return r
    return wrapper


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


@memoize
def memoized_factorial(n):
    return factorial(n)


@pytest.mark.parametrize("inp, result", [(2, 2), (3, 6), (4, 24), (5, 120), (6, 720)])
def test_factorial(inp, result):
    assert factorial(inp) == result


@pytest.mark.parametrize("inp, result, cached", [(2, 2, False),
                                                 (2, 2, True),
                                                 (5, 120, False),
                                                 (5, 120, True),
                                                 (5, 120, True),
                                                 ])
def test_memoized_factorial(mocker, inp, result, cached):
    mock_factorial = mocker.patch("test_decorators.factorial")
    mock_factorial.return_value = result
    memoized_factorial(inp)
    from_cache = True if mock_factorial.call_count == 0 else False
    assert from_cache == cached


def notification_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"decorator: function {func} to be called with args {args} {kwargs}")
        r = func(*args, **kwargs)
        print(f"decorator: function {func} finished")
        return r
    return wrapper


@notification_decorator
def function_logic(a, b, c=[]):
    print(f"work with {a}, {b} and {c} ...")
    return a+b


def notification_decorator_parametrized(decorator_arg):
    def the_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"decorator: function {func} to be called with args {args} {kwargs}, decorator arg: {decorator_arg}")
            r = func(*args, **kwargs)
            print(f"decorator: function {func} finished")
            r += 10
            return r
        return wrapper
    return the_decorator


@notification_decorator_parametrized("decorator_param")
def function_logic_another(a, b, c=[]):
    print(f"work with {a}, {b} and {c} ...")
    return a+b


def test_function_logic_another():
    assert function_logic_another(1, 2) == 13


def signature_preserving_parametrized_decorator(arg1, arg2):
    """
    Signature preserving decorator
    The decorator notification_decorator_parametrized works OK in simple cases like this.

    In the context of pytest (necessity of decorating a pytest test case with a parametrized decorator),
    this approach would not work since the *args, **kwargs would be passed empty (likely due to
    mechanism for passing fixtures in the context of pytest). What works is signature preserving decorator.

    """
    @decorator
    def wrapper(func, *args, **kwargs):
        # *args, **kwargs are available
        func(*args, **kwargs)
    return wrapper
