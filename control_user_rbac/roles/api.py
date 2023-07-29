from ninja import Router
from .models import CustomUser, Role, Permission, UserRole, RolePermission

router = Router()

@router.get("/users/{user_id}/roles/")
def get_user_roles(request, user_id: int):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        return 404, {"detail": "User not found"}

    roles = user.userrole_set.all()
    return {"roles": [role.name for role in roles]}

@router.get("/roles/{role_id}/permissions/")
def get_role_permissions(request, role_id: int):
    try:
        role = Role.objects.get(id=role_id)
    except Role.DoesNotExist:
        return 404, {"detail": "Role not found"}

    permissions = role.rolepermission_set.all()
    return {"permissions": [permission.name for permission in permissions]}
