"""
Pandas experiments above the basic level.

"""


import pandas as pd


def test_simple_map_function_1():
    df = pd.DataFrame(dict(a=[1, 2, 3, 4], b=[5, 6, 7, 8]))
    mask = df.a.map(lambda x: x > 2)
    assert df.loc[mask, "a"].to_list() == [3, 4]


def test_simple_map_function_1():
    df = pd.DataFrame(dict(a=['1', '2', 3, 4], b=[5, 6, 7, 8]))
    mask = df.a.map(type) == str
    assert df.loc[mask, "a"].to_list() == ['1', '2']


def test_define_values_by_dict():
    df = pd.DataFrame(dict(a=[1, 2, 3, 4], b=[5, 6, 7, 8]))
    repl = {1: 11, 2: 22, 4: 55}
    df["new_a"] = df.a.map(repl)
    assert df.loc[df.new_a.notna(), "new_a"].to_list() == [11, 22, 55]
    # the same done via assign and lambda
    df = df.assign(new_aa=lambda x: x["a"].map(repl))
    assert df.loc[df.new_aa.notna(), "new_aa"].to_list() == [11, 22, 55]


def test_replace_series_values_by_map_file():
    """"
    Replace some series values via mapping file.
    the mapping file is delivered in CSV, old_value, new_value pairs

    Want to change values in column 'a'.

    """
    df = pd.DataFrame(index=["i1", "i2", "i3", "i4"])
    df["a"] = [1, 2, 3, 4]
    df["b"] = [5, 6, 7, 8]
    # pair 10, 11 won't be used - no such df["a"] value
    corr_df = pd.DataFrame(dict(old_a=[2, 4, 10], new_a=[0, 9, 11]))
    corr_df = corr_df.set_index("old_a")
    df["_a"] = df.a.map(corr_df.new_a.to_dict())  # index becomes dict key
    mask = df._a.notnull()
    df.loc[mask, "a"] = df.loc[mask, "_a"]
    df = df.drop(columns=["_a"])
    assert df.loc[["i2", "i4"], "a"].to_list() == [0, 9]

