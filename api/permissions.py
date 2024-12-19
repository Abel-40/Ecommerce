from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
  def has_object_permission(self, request, view, obj):
    return True
  
  def has_permission(self, request, view):
    return True