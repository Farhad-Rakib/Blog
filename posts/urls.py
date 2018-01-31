from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.post_list,name = "post_list"),
    url(r'^(?P<id>[0-9]+)/$', views.post_detail, name='post_details'),
]
