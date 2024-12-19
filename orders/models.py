from django.db import models
from products.models import Products
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()
ORDER_STATUS = (
  ("pending","pending"),
  ("Delivered","Delivered")
)
class Orders(models.Model):
  product = models.ForeignKey(to=Products,on_delete=models.CASCADE,null=True,related_name='orders')
  created_by = models.ForeignKey(to=User,on_delete=models.SET_NULL,null=True,related_name='orders')
  created = models.DateTimeField(auto_now=True)
  update = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=20,choices=ORDER_STATUS,default="pending")