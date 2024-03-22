from django.urls import include, path

from .views import *

app_name = 'main'

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
]