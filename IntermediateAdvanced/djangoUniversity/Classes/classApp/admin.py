from django.contrib import admin
from .models import djangoClasses

# register my personally created djangoClasses class
admin.site.register(djangoClasses)
