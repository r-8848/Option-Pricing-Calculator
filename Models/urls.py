from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='Main-Home-Page'),
    path('two_step/',include('Two_step_model.urls')),  
    path('n_step/',include('N_step_model.urls')),
    path('black_scholes/',include('Black_scholes__model.urls')),
]
