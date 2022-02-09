from django.contrib import admin

# Register your models here.

from .models import djangoClasses

# Tells admin how to manage our djangoClasses module
admin.site.register(djangoClasses)
