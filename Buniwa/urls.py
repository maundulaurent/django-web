from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name = 'about'),
    path('team', views.team, name = 'team'),
    path('services', views.services, name = 'services'),
    path('career', views.career, name = 'career'),
    path('contact', views.contact, name = 'contact'),
    path('projects', views.projects, name="projects"),
    path('faqs', views.faqs, name="faqs"),
]
