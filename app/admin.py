from django.contrib import admin
from . models import (Viewer)


@admin.register(Viewer)
class ViewerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']
