from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
<<<<<<< HEAD
from .models import theBlog
=======
from django.contrib.auth.models import User
from .models import Card
>>>>>>> 2a242e0ccc7c1ec90306a6f34bff775db59f3b49
from .models import PortfolioPost
from .models import theTeam



# Create your views here.

def index(request):
    return render(request, 'Buniwa/index.html')

def about(request):
    return render(request, 'Buniwa/about.html')

def team(request):
    cards = theTeam.objects.all()
    return render(request, 'Buniwa/team.html', {'cards': cards})

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
<<<<<<< HEAD
    cards = theBlog.objects.all()
    return render(request, "Buniwa/blog.html", {'cards': cards})


=======
    cards = Card.objects.all()
    return render(request, "Buniwa/blog.html", {'cards': cards})

>>>>>>> 2a242e0ccc7c1ec90306a6f34bff775db59f3b49

def blog_details(request):
    return render(request, "Buniwa/blog_details.html")

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

def portfolio_details(request):
    return render(request, 'Buniwa/portfolio_details.html')

def portfolio(request):
    cards = PortfolioPost.objects.all()
    return render(request, 'Buniwa/portfolio.html', {'cards': cards})