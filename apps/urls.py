from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.views import ClientModelViewSet, CategoryModelViewSet, ProductModelViewSet, MerchantModelViewSet

router = DefaultRouter()
router.register('client', ClientModelViewSet, 'client')
router.register('merchant', MerchantModelViewSet, 'merchant')
router.register('category', CategoryModelViewSet, 'category')
router.register('product', ProductModelViewSet, 'product')

urlpatterns = [
    path('', include(router.urls))
]
