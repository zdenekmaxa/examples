"""
Pandas experiments. Some via doctest some direct unit test cases.


- pytest.mark.skip doens't work here with doctest

- doctest skip - can't find out how to specify a test to skip

- having multiple examples to run, 1 failing fails the whole test,
    doesn't work like pytest parametrize ...

- pytest verbose (-v) doesn't work to show tried values via doctest

"""

import doctest

import pytest
import pandas as pd


def doctest_test():
    """
    a doctest in a docstring
    >>> doctest_test()
    42

    """
    return 42


def factorial(n):
    """
    From doctest documentation, inspiration for reference.

    Return the factorial of n, an exact integer >= 0.

    >>> [factorial(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]

    >>> factorial(30)
    265252859812191058636308480000000

    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Factorials of floats are OK, but the float must be an exact integer:

    >>> factorial(30.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer

    >>> factorial(30.0)
    265252859812191058636308480000000

    It must also not be ridiculously large:

    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n too large

    """
    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


def update(df1, df2):
    """
    update existing column in the df with new values

    >>> df1 = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
    >>> df2 = pd.DataFrame(dict(b=[6, 7]))
    >>> update(df1, df2)
       a  b
    0  1  6
    1  2  7

    only existing columns in the original df are updated
    >>> df1 = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
    >>> df2 = pd.DataFrame(dict(b=[6, 7], c=[8, 9]))
    >>> update(df1, df2)
       a  b
    0  1  6
    1  2  7

    >>> df1 = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
    >>> df2 = pd.DataFrame(dict(a=[1, 2], b=[8, 9]))
    >>> update(df1, df2)
       a  b
    0  1  8
    1  2  9

    """
    # returns nothing, does inplace modification
    df1.update(df2)
    return df1


def update_via_loc(df1, df2):
    """
    indexing must match
    >>> df1 = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
    >>> df2 = pd.DataFrame(dict(a=[1, 2], b=[5, 6], c=[7, 8]))
    >>> update_via_loc(df1, df2)
       a  b
    0  1  5
    1  2  6

    """
    df1.loc[df2.index, ["b"]] = df2.b
    return df1


def update_via_loc_arbitrary_index(df1, df2):
    """
    update via loc via arbirtary column indexing

    >>> df1 = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
    >>> df2 = pd.DataFrame(dict(a=[1, 2], b=[5, 6], c=[7, 8]))
    >>> update_via_loc_arbitrary_index(df1, df2)
       a    b
    0  1  6.0
    1  2  NaN

    This is not what is expected but makes sense since:

    df1 after index set:
           b
        a
        1  3
        2  4

    df2:
           a  b  c
        0  1  5  7
        1  2  6  8

    df2.a is [1, 2] and these indices applied to df2.b return [6, NaN]
    df2.loc[[1, 2], ["b"]]:
        b
            1  6.0
            2  NaN

    will be KeyError in the future.

    """
    df1 = df1.set_index("a")
    df1.loc[df2.a, ["b"]] = df2.b
    return df1.reset_index()


@pytest.mark.parametrize("inpt,output",
                         [((1, 2), 3,),
                          ((3, 4), 7,),
                          ])
def test_summer(inpt, output):
    # plain unit test to be discovered must be in test* module in a test* function
    assert sum(inpt) == output


def test_filter():
    """
    Test DataFrame filter

    """
    df = pd.DataFrame(dict(aa=[1, 2], bb=[3, 4], ab=[5, 6], ba=[7, 8]))
    # df
    #        aa  bb  ab  ba
    #     0   1   3   5   7
    #     1   2   4   6   8
    assert df.filter(regex="c|d").columns.values.tolist() == []
    assert df.filter(regex="c|d").index.tolist() == [0, 1]
    assert df.filter(regex="^a|c|d").columns.values.tolist() == ["aa", "ab"]


def selection(df):
    """
    Test selection options.
    >>> df = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
    >>> selection(df)
       a  b
    1  2  4

    """
    s1 = df[df["a"] > 1]
    s2 = df[df.a > 1]
    assert s1.equals(s2)
    s2 = df.loc[df["a"] > 1, :]
    assert s1.equals(s2)
    s2 = df.loc[df.a > 1, :]
    assert s1.equals(s2)
    s2 = df.query("a > 1")
    assert s1.equals(s2)
    return s1


if __name__ == "__main__":
    # when run directly via doctest: python module.py
    # with -v prints all tired values and expected output
    doctest.testmod()
