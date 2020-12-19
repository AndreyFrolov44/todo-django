from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, TodoBlock, TodoItem


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    list_filter = ('username', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(TodoBlock)
class TodoBlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'date_add',)


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'block', 'date_add',)

