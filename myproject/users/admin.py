from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','email', 'full_name', 'about', 'company', 'job_title', 'country', 'phone')
    search_fields = ('user__username', 'full_name', 'company', 'job_title')

    def email(self, obj):
        return obj.user.email


admin.site.register(UserProfile, UserProfileAdmin)
