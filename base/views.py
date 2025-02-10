from django.shortcuts import render
from django.http import HttpResponse

# Sample data for rooms
rooms = [
    {'id': 1, 'name': 'Let’s Learn Python!'},
    {'id': 2, 'name': 'Design with Me'},
    {'id': 3, 'name': 'Frontend Developers'},
]

# Home View
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

# Room View (Dynamic)
def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
