from django.urls import include, path

from main.views import *

app_name = 'main'

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
]