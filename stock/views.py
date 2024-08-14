from django.contrib.auth.models import User
from djoser.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from .models import Stock, Category, Equipment
from .permissions import ReadOnly, IsAdminOrReadOnly, IsAuthenticatedAndReadOnlyOrAdmin
from .serializers import (
    StockSerializer,
    CategorySerializer,
    EquipmentSerializer,
    # UserSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):
    """Категории оборудования"""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedAndReadOnlyOrAdmin]


class StockViewSet(viewsets.ModelViewSet):
    "Склады"
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [IsAuthenticatedAndReadOnlyOrAdmin]


class EquipmentViewSet(viewsets.ModelViewSet):
    "Оборудование"
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAuthenticatedAndReadOnlyOrAdmin]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedAndReadOnlyOrAdmin]
