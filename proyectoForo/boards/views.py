from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return HttpResponse(""" <!DOCTYPE html><html><body><h1>My First </h1><p>My first paragraph.</p></body></html> """)

def adios(request):
    return HttpResponse('Bye')