"""
Views definitions.

"""

import datetime

from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

from models import Question


def get_datetime(request):
    return HttpResponse("current time: '%s'" % datetime.datetime.now())


def get_questions(request):
    all_qs = Question.objects.all()
    #json.dumps(all_qs)  # can't do - error that it's not JSON serializable
    data = serializers.serialize("json", all_qs)
    return HttpResponse(data, content_type="application/json")


def get_question(request, question_id=0):
    try:
        q = Question.objects.get(pk=question_id)  # identical to id=1
    except Exception, ex:
        r = HttpResponseNotFound()
        r.write("Error, reason: '%s'" % ex)
        return r
    else:
        data = serializers.serialize("json", [q])  # must be iterable
        return HttpResponse(data, content_type="application/json")