from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name="black_scholes_homepage"),
    path('pricing_option/',views.pricing,name="black_scholes_result"),
]
