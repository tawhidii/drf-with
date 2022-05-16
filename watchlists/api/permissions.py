
from urllib import request
from rest_framework import permissions

# class IsStaffOrReadOnly(permissions.BasePermission):
#     # pass
#     # def has_permission(self, request, view):
#     #     if request.user.is_staff:
#     #         return True
#     #     else:
#     #         return request.method in permissions.SAFE_METHODS

#     def has_object_permission(self, request, view, obj):
#         print(obj)
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         else:
#             return request.user == obj

# Example of object lever permission 
class ReviewIsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return obj.review_user == request.user
        



