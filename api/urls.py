from django.urls import path,include
from .views import UserViewset,ProductViewSet,CategoryViewSet,OrderViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
router = DefaultRouter()
router.register(r"read_user",UserViewset)
router.register(r"product",ProductViewSet)
router.register(r"category",CategoryViewSet)
router.register(r"order",OrderViewSet)
urlpatterns = [
  path('',include(router.urls)),
  path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]