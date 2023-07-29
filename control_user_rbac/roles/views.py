from ninja import Router

router = Router()

@router.get("/users/{user_id}/roles/")
def get_user_roles(request, user_id: int):
    # Implemente a lógica para retornar as funções associadas ao usuário
    # Resto da implementação...
    pass

@router.get("/roles/{role_id}/permissions/")
def get_role_permissions(request, role_id: int):
    # Implemente a lógica para retornar as permissões associadas à função
    # Resto da implementação...
    pass
