"""
This test module uses Django-recommended
django.test.TestCase which is a derivation of Python standard library
unittest.TestCase.

Run via:
    python manage.py test
        the test is picked up out-of-the box, no other settings necessary

    py.test tests/
        fails with You must either define the environment variable
            DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
        so: export DJANGO_SETTINGS_MODULE="settings"
        prior to running is necessary (this is what manage.py does)
        OR
        create pytest.ini file with the same content - setting of DJANGO_SETTINGS_MODULE

"""

import datetime

from django.test import TestCase
from pollsapp.models import Question


class QuestionTestCase(TestCase):
    def setUp(self):
        Question.objects.create(question_text="How are you?",
                                pub_date=datetime.datetime(year=2015, month=11, day=28))

    def test_model_basic(self):
        """
        Test that the model entity added in set up method is present.

        """
        qs = Question.objects.all()
        for q in qs:
            if "How are you?" == q.question_text:
                break
        else:
            self.fail("The entity created in setup is not present in the database.")
