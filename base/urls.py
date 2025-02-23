from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),  # ✅ Fixed missing view function
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),  # ✅ Removed duplicate entry
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
        path('update-user/', views.updateUser, name='update-user'),

            # 🌐 API URLs
    path('api/', views.apiOverview, name="api-overview"),
    path('api/users/', views.getUsers, name="api-users"),
    path('api/user/<str:pk>/', views.getUser, name="api-user"),
    path('api/rooms/', views.getRooms, name="api-rooms"),
    path('api/room/<str:pk>/', views.getRoom, name="api-room"),
    path('api/messages/', views.getMessages, name="api-messages"),

]
