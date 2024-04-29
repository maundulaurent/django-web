from django.contrib import admin
from .models import theBlog
from .models import PortfolioPost
from.models import theTeam

admin.site.register(theBlog)
admin.site.register(PortfolioPost)
admin.site.register(theTeam)
