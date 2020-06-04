from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin 



class User(AbstractBaseUser, PermissionsMixin):
    pass 






class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    users = models.ManyToManyField(User, blank=True)
    
    def __str__(self):
        return self.text




