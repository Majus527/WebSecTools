from django.urls import path
from . import views

urlpatterns = [
    path('vulnscan', views.vulnscan, name="vulnscan"),

]

