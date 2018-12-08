from django.contrib import admin

# Register your models here.

from .models import MyUrlShortner

admin.site.register(MyUrlShortner)