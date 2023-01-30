from django.urls import path
from . import views

app_name = "app"

from . import views
from rest_framework import routers
from django.urls import path, include


urlpatterns = [

    #
    path('sign-up/', views.SignUp),
    path('sign-in/', views.SignIn),
    path('reset/', views.Reset),
    path('verify/', views.Verify),
    path('edit-profile/', views.EditProfile),

    
    ]