from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('rooms/', views.getRooms, name="get-rooms"),
    path('room/<str:pk>/', views.getRoom, name="get-room"),
    path('users/', views.getUsers, name="get-users"),
    path('user/<str:pk>/', views.getUser, name="get-user"),
    path('messages/', views.getMessages, name="get-messages"),
]
