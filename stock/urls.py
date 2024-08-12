from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from .views import StockViewSet, CategoryViewSet, EquipmentViewSet
app_name = 'stock'

router = routers.SimpleRouter()
router.register(r"stock", StockViewSet)
router.register(r"category", CategoryViewSet)
router.register(r"equipment", EquipmentViewSet)
# router.register(r"users", UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("v1/", include(router.urls), name='v1'),
    path('v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

]
