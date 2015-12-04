"""
This module uses py.test unit testing framework.
It depends only on proper module / methods / functions naming
and no special class inheritance (as opposed to unittest).

Run via:
    py.test tests/
        (depends on pytest.ini file specifying DJANGO_SETTINGS_MODULE)

"""

import datetime

import pytest

from pollsapp.models import Question


@pytest.mark.django_db
class TestQuestion(object):
    """
    Test object encapsulating test cases in methods.

    """

    def setup_method(self, method):
        pass

    def test_model_basic(self):
        """
        Test that the model entity added in set up method is present.

        """
        # as opposed to unittest which created this object in setUp(),
        # create it here at the test case itself
        t = "How are you?"
        Question.objects.create(question_text=t,
                                pub_date=datetime.datetime(year=2015, month=11, day=28))
        try:
            q = Question.objects.get(question_text=t)
        except Question.DoesNotExist:
            pytest.fail("The entity created in setup is not present in the database.")
        assert q.question_text == t

    @pytest.mark.skipif(True,
                        reason="Need to redefine arithmetic first. Tracked on a ticket #XX")
    def test_division_by_zero(self):
        """
        Demonstrate skipping a problematic / failing test, a test still under development.

        """
        res = 100/0
        # continue ... :)


@pytest.mark.django_db  # must be here
def test_model_basic_function():
    """
    Test that the model entity added in set up method is present.
    Test in a function.

    """
    # as opposed to unittest which created this object in setUp(),
    # create it here at the test case itself
    t = "How are you?"
    Question.objects.create(question_text=t,
                            pub_date=datetime.datetime(year=2015, month=11, day=28))
    try:
        q = Question.objects.get(question_text=t)
    except Question.DoesNotExist:
        pytest.fail("The entity created in setup is not present in the database.")
    assert q.question_text == t