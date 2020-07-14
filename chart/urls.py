from django.urls import path
from . import views

urlpatterns = [
    path('pie_chart/', views.pie_chart, name='pie-chart'),
    path('', views.home, name='home'),
    path('population-chart/', views.population_chart, name='population-chart'),
]