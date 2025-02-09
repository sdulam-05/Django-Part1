from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('room/', views.room, name='room'),  # Room page
]
