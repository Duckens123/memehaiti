from django.shortcuts import render
from rest_framework import generics,permissions
from .views import *

class IsAuthenticatedUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Vérifie si l'utilisateur est authentifié
        is_authenticated = super().has_permission(request, view)
        
        # Vérifie si le jeton JWT est présent dans l'en-tête Authorization
        has_jwt = 'Authorization' in request.headers and 'Bearer' in request.headers['Authorization']
        
        return is_authenticated and has_jwt


