from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import CustomUserModel

@admin.register(CustomUserModel)
class CustomAdmin(UserAdmin):
    """docstring for CustomAdmin.UserAdmin"""
    # model = CustomUserModel
    list_display = ('id', 'username', 'email')
    fieldsets = UserAdmin.fieldsets + (
        ('Change Avatar', {
            'fields' : ['avatar']
        }),
    )
