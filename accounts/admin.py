from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username',]
    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nick_name',)}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nick_name',)}),
    )
