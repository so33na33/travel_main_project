from django.contrib import admin

# Register your models here.
from .models import django
from .models import place
admin.site.register(django)
admin.site.register(place)