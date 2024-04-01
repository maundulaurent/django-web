from django.shortcuts import render


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

def projects(request):
    return render(request, "Buniwa/projects.html")

def faqs(request):
    return render(request, "Buniwa/faqs.html")

def blog(request):
    return render(request, "Buniwa/blog.html")