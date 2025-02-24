from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from base.models import Room, Message

# Room Serializer
class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'  # Include all fields

# User Serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Message Serializer
class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
