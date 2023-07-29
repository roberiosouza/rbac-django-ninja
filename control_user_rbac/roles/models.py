from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Campos adicionais para o usuário, se necessário
    pass

class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # Outros campos relevantes para a função, se necessário

class Permission(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # Outros campos relevantes para a permissão, se necessário

class UserRole(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
