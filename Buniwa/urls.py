from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name = 'about'),
    path('team', team, name = 'team'),
    path('services', services, name = 'services'),
    path('career', career, name = 'career'),
    path('contact', contact, name = 'contact'),
    path('projects', projects, name="projects"),
]
