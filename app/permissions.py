from rest_framework.permissions import BasePermission, SAFE_METHODS


class FoodPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return True


class FoodTypePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return True


class CommentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            return True