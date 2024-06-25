from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name="N_step_homepage"),
    path('pricing_option/',views.pricing,name="N_step_result"),
]
