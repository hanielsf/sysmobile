# Django
from django.urls import path
from django.contrib.auth import views as auth_views

# Views Core
from . import views

app_name = 'core'
urlpatterns = [

    #  Login / Logout
    path('sign-in/', views.login_user, name='sign-in'),
    path('sign-out/',
         auth_views.logout,
         {'next_page': '/'},
         name='sign-out'),
]
