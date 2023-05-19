from django.urls import path
from . import views

urlpatterns = [ path('ask_me/', views.ask_me, name='ask_me'),
]