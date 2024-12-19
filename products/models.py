from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Category(models.Model):
  # CATEGORY_CHOICES = (
  #   ("clothes","clothes"),
  #   ("electronics","electronics"),
  #   ("food","food"),
  #   ("Kitchen","kitchen")
  # )
  name = models.CharField(unique=True,max_length=50)

  def __str__(self):
    return self.name

class Products(models.Model):
  name = models.CharField(unique=True, max_length=50)
  description = models.CharField(max_length=50,blank=True,null=True)
  category = models.ForeignKey(to=Category,on_delete=models.CASCADE,related_name='products')#category.products
  price = models.DecimalField(max_digits=10,decimal_places=2)
  created_by = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='products')#user.products
  created = models.DateTimeField(auto_now=True)
  updated = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name