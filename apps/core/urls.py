# Django
from django.urls import path, include
from django.contrib.auth import views as auth_views

# Rest-Framework
from rest_framework.authtoken import views as rest_framework_views

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

    # Token Rest-Framework
    path('get_auth_token/', rest_framework_views.obtain_auth_token, name='get_auth_token'),
    path('rest-auth/', include('rest_auth.urls')),
]
