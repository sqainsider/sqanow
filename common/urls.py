from django.urls import path
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),


    #     path('city/', views.CityListView.as_view(), name='city_list'),
    #     path('city/add/', views.CityCreateView.as_view(), name='city_add'),

    #     path('ajax/load-states/', views.load_states, name='ajax_load_states'),
    #

]
