from django.contrib import admin

# Register your models here.

from .models import Note

# to see out model in the admin panel
admin.site.register(Note)