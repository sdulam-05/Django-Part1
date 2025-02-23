from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from .models import Room, Topic, Message
from .forms import RoomForm, CustomUserCreationForm


# Home Page (List all Rooms)
def home(request):
    q = request.GET.get('q') if request.GET.get('q') else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)


# Individual Room Page (Messages and Participants)
def room(request, pk):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all().order_by('-created')

    if request.method == "POST":
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        return redirect('room', pk=room.id)

    context = {'room': room, 'messages': messages}
    return render(request, 'base/room.html', context)


# Create a New Room
@login_required(login_url='login')
def createRoom(request):
    topics = Topic.objects.all()  # Fetch all available topics
    form = RoomForm()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')  # Get topic input from form
        topic, created = Topic.objects.get_or_create(name=topic_name)  # Create or fetch topic

        # Create the room with selected topic
        room = Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)


# Update an Existing Room
@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()

    if request.user != room.host:
        return HttpResponse("You are not allowed to edit this room!")

    if request.method == 'POST':
        topic_name = request.POST.get('topic')  # Get topic input
        topic, created = Topic.objects.get_or_create(name=topic_name)  # Create/fetch topic

        # Update room details
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()

        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_form.html', context)


# Delete a Message (Only Owner Can)
@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("You are not allowed to delete this message!")

    if request.method == "POST":
        room_id = message.room.id  # Get the room ID before deleting the message
        message.delete()
        return redirect('room', pk=room_id)  # Redirect back to the correct room

    return render(request, 'base/delete.html', {'obj': message})


# User Login
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials!')

    return render(request, 'base/login_register.html', {'page': 'login'})


# User Logout
def logoutUser(request):
    logout(request)
    return redirect('home')


# User Registration
def registerPage(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration.')

    return render(request, 'base/login_register.html', {'form': form})
