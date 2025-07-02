# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsActiveStaff(permissions.BasePermission):
    """Проверяет, что пользователь model:users.models.CustomUser является автивным (is_active=True)."""

    message = "Доступ открыт только автивным сотрудникам!"

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
