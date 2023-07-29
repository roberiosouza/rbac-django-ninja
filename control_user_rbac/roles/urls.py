from django.urls import path
from ninja import Router
from . import views

router = Router()

router.add_api_view("/users/{user_id}/roles/", views.get_user_roles)
router.add_api_view("/roles/{role_id}/permissions/", views.get_role_permissions)

urlpatterns = [
    path("api/", router.urls),
]
