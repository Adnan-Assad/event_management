from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.
 

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', {'fields': ('phone_number', 'profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)