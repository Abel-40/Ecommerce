from rest_framework import serializers
from django.contrib.auth import get_user_model
from products.models import Products,Category
from orders.models import Orders
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','email','username')
    
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Products
    fields = '__all__'
    
class CategorySerializer(serializers.ModelSerializer):
  products_in_category = ProductSerializer(many=True,read_only=True)
  class Meta:
    model = Category
    fields = ('id','name','products_in_category')
    
class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Orders
    fields = ('product','created_by','created','update')