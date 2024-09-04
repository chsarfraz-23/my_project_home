from django.contrib.auth.models import User
from rest_framework.request import Request


def validate_permission(request: Request, permission: str) -> bool:
    return request.user.has_perm(permission)


def user_in_group(user: User, role_name) -> bool:
    return user.groups.filter(name=role_name).exists()
