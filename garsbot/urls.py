# urls.py
from django.urls import path
from .views import ask_garsbot

urlpatterns = [
    path('ask/', ask_garsbot, name='ask_garsbot'),
]