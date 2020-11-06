from django.shortcuts import render
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.

def home(request):
    return render(request, 'base.html')
