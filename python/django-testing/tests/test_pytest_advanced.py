"""
Module with pytest style advanced findings / observations.

"""


import datetime

import pytest
from django.db import connection

import settings
from pollsapp.models import Question
from factories import QuestionFactory, ChoiceFactory

# this is the name of the database as defined in the settings.py file
original_db_name = settings.DATABASES["default"]["NAME"]


@pytest.mark.django_db
class TestAdvanced(object):

    def setup_method(self, method):
        pass

    def test_database_name(self):
        """
        The original database name defined in settings is used but
        the tests run in a fresh database called "test_" + ORIGINAL_NAME

        """
        # settings.DATABASES["default"]["NAME"]
        # is redefined at this stage (see where original_db_name comes from)
        # original db name needs to have "test_" string added to equal to the current db name
        assert "test_" + original_db_name == settings.DATABASES["default"]["NAME"]
        assert settings.DATABASES["default"]["NAME"] == connection.settings_dict["NAME"]

    def test_migrations_are_run(self):
        """
        Demonstrate that the migrations are run (on a fresh database).

        """
        # migration 0002 adds two objects into Question model
        qs = Question.objects.all()
        assert len(qs) == 2
        t = "What is the time?"
        Question.objects.create(question_text=t,
                                pub_date=datetime.datetime(year=2015, month=11, day=28))
        qs = Question.objects.all()
        assert len(qs) == 3
        qs = Question.objects.filter(question_text__startswith=t)
        assert len(qs) == 1
        q = qs[0]
        # primary key
        assert q.pk == q.id

    def test_data_interaction(self):
        Question.objects.create(question_text="How are you?",
                                pub_date=datetime.datetime(year=2015, month=11, day=28))
        qs = Question.objects.filter(question_text__startswith="How are you?")
        q = qs[0]
        q.question_text = "What's new?"
        q.save()
        qs = Question.objects.filter(question_text__startswith="How are you?")
        assert len(qs) == 0
        # useful Model._meta
        assert q._meta.get_all_field_names() == ['choice', u'id', 'pub_date', 'question_text']
        assert q._meta.model_name == "question"

    def test_with_factories(self):
        """
        Demonstrates interaction with factory_boy library
        for managing test data by means of test factory objects.

        """
        q = QuestionFactory.create()  # does save()
        qs = Question.objects.filter(question_text__startswith="What is your name?")
        assert len(qs) == 1
        qs.delete()
        q = QuestionFactory.build()  # does not save()
        qs = Question.objects.filter(question_text__startswith="What is your name?")
        assert len(qs) == 0
        print QuestionFactory.create
        #q = QuestionFactory.create()  # does save()
