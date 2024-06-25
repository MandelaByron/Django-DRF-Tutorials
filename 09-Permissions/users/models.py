from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from .managers import CustomUserManager
from players.models import Player

class User(AbstractBaseUser, PermissionsMixin):
    favorite_players = models.ManyToManyField(Player, related_name='fans')
           
    public_id  = models.UUIDField(db_index=True, unique=True, editable=False, default=uuid.uuid4)

    first_name = models.CharField(max_length=250)
    
    last_name = models.CharField(max_length=250)
    
    email = models.EmailField(db_index=True, unique=True)
    
    is_staff = models.BooleanField(default=False)
    
    is_active = models.BooleanField(default=True)
    
    is_superuser =models.BooleanField(default=False)
      
    date_joined = models.DateTimeField(auto_now_add=True) #set the time to when the object is first created
    
    updated = models.DateTimeField(auto_now=True)#set the time to when the object is saved
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['first_name', "last_name"]
    
    objects =  CustomUserManager()