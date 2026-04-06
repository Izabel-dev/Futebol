from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_times, name='lista_times'),  # URL base do app
]