from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

"""
Voy a crear mi propio modelo de usuario, para ello voy a heredar de la clase AbstractUser

"""
class UsuarioManager(BaseUserManager):
    """
    Clase que me permite crear usuarios y guardarlos en la base de datos
    """
    def create_user(self, username,email, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email')
        user = self.model(
            username = username,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password):
        """
        crea y guarda un superusuario con el email y password dados
        """
        user = self.create_user(
            username=username,
            email=email,
            password=password,
           
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

#clase usuario

class Usuario(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


class SuperUsuario(Usuario):
    class Meta:
        proxy = True
        
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

