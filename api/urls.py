from django.urls import path
from . import views

urlpatterns = [ path('ask_me/', views.generate_images, name='ask_me'),
]