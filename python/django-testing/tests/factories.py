"""
Defines test object factories.
Uses factory_boy library.

"""

import factory

from pollsapp.models import Question
from pollsapp.models import Choice


class QuestionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Question

    question_text = "What is your name?"
    pub_date = "2014-08-21T18:47:04.271"


class ChoiceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Choice

    question = factory.SubFactory(QuestionFactory)
    choice_text = "Babice"
    votes = 10