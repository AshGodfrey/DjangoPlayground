
from django.contrib import admin
from django.urls import path, include # new
from .views import homePageView
urlpatterns = [
    path('', homePageView, name='home')
]