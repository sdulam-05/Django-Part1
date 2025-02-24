from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'email', 'username', 'name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'name', 'bio')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )

admin.site.register(User, CustomUserAdmin)
