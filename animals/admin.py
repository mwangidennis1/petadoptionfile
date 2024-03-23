from django.contrib import admin
from .models import Animal,AdoptMe

class AnimalAdmin(admin.ModelAdmin):
    list_display=('title','breed','sex','description',)

class AdoptAdmin(admin.ModelAdmin):
    list_display=('adoptFor','caregiver','numberofchildren','allergies','residence','staydaytime',)

admin.site.register(Animal,AnimalAdmin)
admin.site.register(AdoptMe,AdoptAdmin)
