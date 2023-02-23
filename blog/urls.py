from django.urls import path
from . import views

app_name = "blog"

from . import views
from rest_framework import routers
from django.urls import path, include


urlpatterns = [

    #
    path('', views.Index),
    path('add/', views.Add),
    path('edit/', views.Edit),
    path('delete/', views.Delete),

    path('add-comment/', views.AddComment),

    #path('filter/<str:category>/<str:location>/<str:rating>/', views.Filter),
    
    ]