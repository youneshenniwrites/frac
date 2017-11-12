from django.contrib import admin

from .models import UserProfile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'date_of_birth', 'profile_photo', '__str__']


admin.site.register(UserProfile, ProfileAdmin)
