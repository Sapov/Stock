from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import StockViewSet, CategoryViewSet, EquipmentViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r"stock", StockViewSet)
router.register(r"category", CategoryViewSet)
router.register(r"equipment", EquipmentViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
]
