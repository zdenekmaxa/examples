"""
from django.conf.urls import url

NOTE:
    there are some changes in the URL treatments between 1.7 to 1.8 Django.

"""

from django.conf.urls import patterns

from pollsapp import views


urlpatterns = patterns(
    '',
    #(r'^admin/', admin.site.urls),
    (r'^datetime/', views.get_datetime),
    (r'^questions/', views.get_questions),
    (r'^question/([0-9]+)$', views.get_question)
)
