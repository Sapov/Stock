from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS, IsAdminUser

from .models import Stock, Category, Equipment
from .serializers import (
    StockSerializer,
    CategorySerializer,
    EquipmentSerializer,
    UserSerializer,
)
from django.contrib.auth.models import Group, User


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [IsAuthenticated | ReadOnly]
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
