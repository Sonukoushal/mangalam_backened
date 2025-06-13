from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self,name,email,password=None):
        if not email:
            raise ValueError("email is required")
        user= self.model(email=self.normalize_email(email),name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects=UserManager()

    USERNAME_FIELD = 'email'
                           
    REQUIRED_FIELDS = ['name']
                             

    def __str__(self):
        return self.email
    
    