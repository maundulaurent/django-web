from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from . forms import SignUpForm

# Create your views here.

def home(request):
    return render(request, "Portal/home.html")

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        
    else:
        form = SignUpForm()
    return render(request, "Portal/signup.html", {'form':form})

def team(request):
    return render(request, "Portal/team.html")