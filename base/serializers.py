from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Room, Message

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Room Serializer
class RoomSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    participants = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = '__all__'

# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    room = RoomSerializer(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'
