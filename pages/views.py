from django.http import HttpResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist

# Create your views here.
def index(request):
    try:
        return render(request, 'pages/index.html')
    except TemplateDoesNotExist:
        return HttpResponse("Template not found")
    #return HttpResponse("index")

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')