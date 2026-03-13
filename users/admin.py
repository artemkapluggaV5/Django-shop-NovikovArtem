from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import Employee


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    list_display = ("get_full_name", "telegram_id")
    ordering = ("email",)

    fieldsets = [
        ('Личная информация', {
            'fields': [
                'last_name', 'first_name', 'telegram_id', 'email'
            ],
        }),
        ('Безопасность', {
            'fields': [
                'password', 'is_active', 'is_staff', 'is_superuser',
            ],
        }),
        ('Права доступа', {
            'fields': ['user_permissions']
        }),
    ]

    add_fieldsets = [
        ('Личная информация', {
            'fields': [
                'email', 'telegram_id', 'password1', 'password2'
            ],
        }),

    ]
