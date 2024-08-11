from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Stock, Category, Equipment
from .serializers import StockSerializer, CategorySerializer, EquipmentSerializer, UserSerializer
from django.contrib.auth.models import Group, User


class StockViewSet(viewsets.ViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EquipmentViewSet(viewsets.ViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

