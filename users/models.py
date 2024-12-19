from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser
# Create your models here.

class UserManager(BaseUserManager):
  def create_user(self,email,password,username=None):
    if not email:
      raise ValueError("Email is required")
    email = self.normalize_email(email)
    username = self.normalize_email(username)
    user = self.model(email=email,username=username)
    
    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self,email,password,username):
    user = self.create_user(email=email,password=password,username=username)
    user.is_staff = True
    user.is_superuser = True
    user.save(using=self._db)
    return user
  
class User(AbstractUser):
  email = models.EmailField(unique=True,max_length=255)
  username = models.CharField(unique=False,max_length=50)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']#we write list of fields that are requeired when we are creating user and supersuser
  objects = UserManager()
  
  def __str__(self):
    return self.username