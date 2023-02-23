from django.urls import path
from . import views

app_name = "business"

from . import views
from rest_framework import routers
from django.urls import path, include


urlpatterns = [

    #
    path('', views.Index),
    path('add/', views.Add),
    path('edit/', views.Edit),
    path('delete/', views.Delete),
    path('all/', views.All),
    path('filter/<str:category>/<str:location>/<str:rating>/', views.Filter),
    path('get/<str:business_id>/', views.Get),
    
    ]