"""
Pandas experiments. Basic ones.

Some via doctest some direct unit test cases.

- pytest.mark.skip doesn't work here with doctest

- doctest skip - can't find out how to specify a test to skip

- having multiple examples to run, 1 failing fails the whole test,
    doesn't work like pytest parametrize ...

- pytest verbose (-v) doesn't work to show tried values via doctest

- python test_various.py -v prints all tried values via doctest

"""


import doctest

import pytest
import pandas as pd


@pytest.fixture
def df():
    return pd.DataFrame(dict(a=[1, 2], b=[3, 4]))


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


def sum_axis_argument(df, axis):
    """
    Test axis argument:
        0 means operation applied to columns, column names are in result index, sum of columns
        1 means operation applied to rows, result index is the same as in the source

    >>> df = pd.DataFrame(dict(a=[1, 2], b=[3, 4]))
    >>> sum_axis_argument(df, None)
    a    3
    b    7
    dtype: int64

    >>> sum_axis_argument(df, 0)
    a    3
    b    7
    dtype: int64

    Source index preserved, operation applied to rows, sum of rows.

    >>> sum_axis_argument(df, 1)
    0    4
    1    6
    dtype: int64

    Apply to series, only axis=0 is allowed, axis=1 - ValueError
    >>> sum_axis_argument(df.a, 0)
    3

    """
    return df.sum(axis=axis)


if __name__ == "__main__":
    doctest.testmod()
