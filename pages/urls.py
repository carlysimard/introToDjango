#!/usr/bin/env python
__author__ = "Carly Simard"

from django.urls import path
from .views import homePageView
urlpatterns = [
    path('', homePageView, name='home')
]