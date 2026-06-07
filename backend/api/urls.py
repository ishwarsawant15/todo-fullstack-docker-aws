# backend/api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.message_list, name='message-list'),
    path('health/', views.health_check, name='health-check'),
]