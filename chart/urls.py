from django.urls import path
from django.contrib import admin

from .views import ChartData, HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/chart/data/', ChartData.as_view(), name='api-view'),

]

