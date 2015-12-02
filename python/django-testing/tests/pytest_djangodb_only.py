"""
Due to it's name, this module won't be collected during whole test suite
run by pytest.

When run on its own, this test runs fine, as part of the test suite, it would fail.

When run on its own, the data in the setup_method go into the main database
(from settings.py) and not the test database!

When run as a part of the test suite (the module needs to be renamed to test_)
there's the following ERROR at setup_method at the database call:
    Failed: Database access not allowed, use the "django_db" mark to enable
    (though the decorator is there)

"""

import datetime

import pytest
from django.db import connection

from pollsapp.models import Question
import settings

# this is the name of the database as defined in the settings.py file
original_db_name = settings.DATABASES["default"]["NAME"]


@pytest.mark.django_db
class TestSetupTeardown(object):

    def setup_method(self, method):
        # it's not using the "test_" + DATABASE_NAME !
        assert connection.settings_dict["NAME"] == settings.DATABASES["default"]["NAME"]
        Question.objects.create(question_text="How are you?",
                                pub_date=datetime.datetime(year=2015, month=11, day=28))
        # this data remains in the main database. if it's adding some unique
        # values, it will fail at the next run

    def test_setup_method(self):
        """
        Data inserted in the setup_method are not part of the transaction
        (unlike unittest setUp() and remain.

        """
        # it is using the "test_" + DATABASE_NAME now
        assert "test_" + original_db_name == settings.DATABASES["default"]["NAME"]
        # migration 0002 adds two objects into Question model
        # what is added in setup_method is not known here
        qs = Question.objects.all()
        assert len(qs) == 2
        # this will be rolled-back at the of the test case transaction
        Question.objects.create(question_text="Is there anybody out there?",
                                pub_date=datetime.datetime(year=2015, month=11, day=28))
        qs = Question.objects.all()
        assert len(qs) == 3

    def teardown_method(self, method):
        return
        # this call will fail with: Failed: Database access not allowed, use the "django_db" mark to enable
        # although the decorator is there
        qs = Question.objects.all()

    @classmethod
    def teardown_class(cls):
        return
        qs = Question.objects.all()