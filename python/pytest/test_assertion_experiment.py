"""
1)
AssertionError or other Exception occurring in setup_method
can't be caught and handled by the test class code.

2)
AssertionError or other Exception occurring in a particular test
can, however, be handled by the test case code itself.

If the first case happens, the output seems to be lost.

The 2) behaviour is normal.

The 1) behaviour was observed on jenkins run tests and
can't be reproduced by this stand-alone script, both exceptions
can be caught whether it happens in test case or setup_method.

Just run py.test -s
in the directory.

"""


class TestCaseMine(object):
    def setup_method(self, method):
        print "setup_method, test case being run: %s" % method.__name__
        try:
            assert 1 == 2
        except AssertionError:
            print "caught AssertionError in setup_method"

    def teardown_method(self, method):
        print "teardown_method, test case finished: %s" % method.__name__

    def test_case_1(self):
        try:
            assert 3 == 4
        except AssertionError:
            print "caught AssertionError in test_case_1"
