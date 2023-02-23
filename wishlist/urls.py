from django.urls import path
from . import views

app_name = "wishlist"

from . import views
from rest_framework import routers
from django.urls import path, include


urlpatterns = [

    #
    path('add/', views.Add),
    path('get/<str:auth_code>/<int:wishlist_id>/', views.Get),
    path('all/<str:auth_code>/', views.All),

]