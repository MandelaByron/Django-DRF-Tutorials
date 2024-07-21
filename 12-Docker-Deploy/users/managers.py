from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.forms import ValidationError

class CustomUserManager(BaseUserManager):
    
    def get_object_by_public_id(self, public_id):
        try:
            instance =  self.get(public_id=public_id)
            
            return instance
        except ObjectDoesNotExist:
            raise Http404("Object Does not exist")
        
        except (ValueError, TypeError, ValidationError):
            raise Http404("Invalid public_id")
            
        
    
    def create_user(self,email, first_name, last_name, password=None, **extra_fields):
        if email is None:
            raise ValueError("Email is required")
        
        if first_name is None:
            raise ValueError("First Name is required")
        
        if last_name is None:
            raise ValueError("Last Name is required")
        
        email = self.normalize_email(email)
        
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        
        user.set_password(password)
        
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self,email, first_name, last_name, password=None, **extra_fields ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        return self.create_user(email=email, first_name=first_name,last_name=last_name ,password=password, **extra_fields)
        
        