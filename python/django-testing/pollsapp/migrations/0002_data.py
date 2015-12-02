# -*- coding: utf-8 -*-
"""
Load some initial data into database tables.

NOTE:
    - to get rid of the timezone warning:
        from django.utils import timezone
        pub_date=timezone.now()

"""

from __future__ import unicode_literals
import datetime

from django.db import migrations


def fill_in_data(apps, schema_editor):
    Question = apps.get_model("pollsapp", "Question")
    q = Question(question_text="What is happiness?",
                 pub_date=datetime.datetime(year=2015, month=11, day=28))
    q.save()
    q = Question(question_text="Which colour is the best?",
                 pub_date=datetime.datetime(year=2015, month=11, day=29))
    q.save()

    print "migration: model 'Question' data insert OK"


class Migration(migrations.Migration):

    dependencies = [("pollsapp", "0001_initial")]

    operations = [migrations.RunPython(fill_in_data)]