from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Home Page</h1>')

def test_page(request):
    return HttpResponse('<h1>Test Page</h1>')