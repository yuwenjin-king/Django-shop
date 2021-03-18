# oding = utf-8
# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/$', views.Register_View.as_view()),
]