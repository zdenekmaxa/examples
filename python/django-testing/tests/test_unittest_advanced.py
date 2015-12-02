"""
This test module uses Django-recommended

django.test.TestCase which is a derivation of Python standard library
unittest.TestCase.

This module shows advanced findings / observations.

"""

import datetime

from django.test import TestCase
from django.db import connection

from pollsapp.models import Question
import settings

# this is the name of the database as defined in the settings.py file
original_db_name = settings.DATABASES["default"]["NAME"]


class AdvancedTestCase(TestCase):

    def setUp(self):
        pass

    def test_database_name(self):
        """
        The original database name defined in settings is used but
        the tests run in a fresh database called "test_" + ORIGINAL_NAME

        """
        # settings.DATABASES["default"]["NAME"]
        # is redefined at this stage (see where original_db_name comes from)
        # original db name needs to have "test_" string added to equal to the current db name
        self.assertEqual("test_" + original_db_name, settings.DATABASES["default"]["NAME"])
        self.assertEqual(settings.DATABASES["default"]["NAME"], connection.settings_dict["NAME"])

    def test_migrations_are_run(self):
        """
        Demonstrate that the migrations are run (on a fresh database).

        """
        # migration 0002 adds two objects into Question model
        qs = Question.objects.all()
        self.assertEqual(len(qs), 2)
        t = "What is the time?"
        Question.objects.create(question_text=t,
                                pub_date=datetime.datetime(year=2015, month=11, day=28))
        qs = Question.objects.all()
        self.assertEqual(len(qs), 3)
        qs = Question.objects.filter(question_text__startswith=t)
        self.assertEqual(len(qs), 1)
        q = qs[0]
        # primary key
        self.assertEqual(q.pk, q.id)