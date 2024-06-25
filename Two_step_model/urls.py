from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name="Two_step_homepage"),
    path('pricing_option/',views.pricing,name="Two_step_result"),
]
