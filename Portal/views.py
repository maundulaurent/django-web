from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
# from . forms import SignUpForm

# Create your views here.

def home(request):
    return render(request, "Portal/home.html")

def signup(request):
    return render(request, "Portal/signup.html")

def team(request):
    return render(request, "Portal/team.html")
