from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from base.models import Room, Message
from .serializers import RoomSerializer, UserSerializer, MessageSerializer

# API Overview
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List Rooms': '/api/rooms/',
        'Get Room': '/api/room/<str:pk>/',
        'List Users': '/api/users/',
        'Get User': '/api/user/<str:pk>/',
        'List Messages': '/api/messages/',
    }
    return Response(api_urls)

# ✅ Get All Users
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

# ✅ Get a Single User
@api_view(['GET'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

# ✅ Get All Rooms
@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

# ✅ Get a Single Room
@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)

# ✅ Get All Messages
@api_view(['GET'])
def getMessages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)
