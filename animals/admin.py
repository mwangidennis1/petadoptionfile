from django.contrib import admin
from .models import Animal

class AnimalAdmin(admin.ModelAdmin):
    list_display=('title','breed','sex','description',)

admin.site.register(Animal,AnimalAdmin)
