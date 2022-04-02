from django.shortcuts import render
from django.db import connection

# Create your views here.
def xyz(request):
    return render(request, "index.html")
def login(request):
    return render(request, "login.html")
def signup(request):
    return render(request, "signup.html")

