"""
from django.conf.urls import url

urlpatterns = [
    url(r'^articles/([0-9]{4})/$', views.year_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]

For example, if a user requested the URL /articles/2005/05/39323/
Django would call the function news.views.article_detail(request, '2005', '05', '39323').

NOTE:
    there are some changes in the URL treatments between 1.7 to 1.8 Django,
    was getting 'no pattern found error' ...

"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

from pollsapp import views


urlpatterns = patterns(
    '',
    (r'^admin/', admin.site.urls),  # ??
    (r'^datetime/', views.get_datetime),
    (r'^questions/', views.get_questions),
    (r'^question/([0-9]+)$', views.get_question)
)
