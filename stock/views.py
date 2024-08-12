from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticated,
    SAFE_METHODS,
    IsAdminUser,
)

from .models import Stock, Category, Equipment
from .serializers import (
    StockSerializer,
    CategorySerializer,
    EquipmentSerializer,
    UserSerializer,
)


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, ReadOnly]


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticated, ReadOnly]


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAuthenticated, ReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
