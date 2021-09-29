#!/usr/bin/env python
__author__ = "Carly Simard"

from django.urls import path
from .views import homePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'), # new
    path('', homePageView.as_view(), name='home'),
]