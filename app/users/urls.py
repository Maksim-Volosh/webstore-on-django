from django.urls import include, path

from users.views import *

app_name = 'users'

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('profile/', profile, name="profile"),
    path('logout/', logout, name="logout"),
]