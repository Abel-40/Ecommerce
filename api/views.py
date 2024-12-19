from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,ProductSerializer,OrderSerializer,CategorySerializer,Products,Orders,Category
from rest_framework.permissions import IsAuthenticated
User = get_user_model()
# Create your views here.

class UserViewset(ReadOnlyModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  
class ProductViewSet(ModelViewSet):
  queryset = Products.objects.all()
  serializer_class = ProductSerializer
  permission_classes = [IsAuthenticated]
  
class CategoryViewSet(ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  
class OrderViewSet(ModelViewSet):
  queryset = Orders.objects.all()
  serializer_class = OrderSerializer