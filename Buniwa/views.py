from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'Buniwa/index.html')

def about(request):
    return render(request, 'Buniwa/about.html')

def team(request):
    return render(request, 'Buniwa/team.html')

def services(request):
    return render(request, 'Buniwa/services.html')

def career(request):
    return render(request, 'Buniwa/career.html')

def contact(request):
    return render(request, 'Buniwa/contact.html')

@login_required(login_url="dash")
def projects(request):
    return render(request, "Buniwa/projects.html")

def faqs(request):
    return render(request, "Buniwa/faqs.html")

def blog(request):
    return render(request, "Buniwa/blog.html")

def dash(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        email=request.POST.get('email')
        user=authenticate(request, username=username, password=pass1, email=email)
        if user is not None:
            login(request,user)
            return redirect('projects')
        else:
            return redirect('dash')
    return render(request, "Buniwa/dash.html")

def user_logout(request):
    logout(request)
    return redirect('dash')

def realp(request):
    return render(request, 'Buniwa/realp.html')