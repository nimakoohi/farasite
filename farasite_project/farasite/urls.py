from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('services/', views.services_view, name='services'),
    path('news/', views.news_view, name='news'),
    path('contact/', views.contact_view, name='contact'),
]