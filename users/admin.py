# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'country', 'is_staff', 'is_active']
