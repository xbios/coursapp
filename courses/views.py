from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_view(request):
    return HttpResponse("Hello, world. Anasayfa.")

def kurslar(request):
    return HttpResponse("Kurslar")
