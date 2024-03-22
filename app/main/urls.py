from django.urls import include, path

from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
]