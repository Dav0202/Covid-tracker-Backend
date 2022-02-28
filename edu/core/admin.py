from django.contrib import admin
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name','is_staff','is_student']
    fieldsets = (
        (None, {
            'fields': (
                'email', 'password'
            )
        }),
        (_('Personal Info'), {
            'fields': (
                'name','classs','address'
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser','is_student',
            )
        }),
        (_('Important dates'), {
            'fields': (
                'last_login',
            )
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('email', 'name')


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Student)
# Register your models here.
