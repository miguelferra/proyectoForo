from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Board
def home(request):
    boards = Board.objects.all()
    boards_names = list()

    return render(request, 'home.html', {'boards':boards})

def adios(request):
    return HttpResponse('Bye')