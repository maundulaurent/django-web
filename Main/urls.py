from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Buniwa.urls')),
    path('Portal/', include('Portal.urls')),
]