from django.conf.urls import patterns, include, url, handler404
from seedme.views import *

urlpatterns = [
        url(r'^$', index, name='index'),
        ]
