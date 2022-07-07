from django.urls import path 
from .import views

urlpatterns =[


    path('home/', views.Home, name='Home'),
    path('', views.search_result , name='search_result'),
    path('', views.Details, name='Details')



]