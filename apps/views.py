from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.viewsets import ModelViewSet

from apps.models import Category, Product, User
from apps.permissions import IsOwner
from apps.serializers import CategoryModelSerializer, ProductModelSerializer, ClientModelSerializer, \
    MerchantModelSerializer, CreateProductModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = DjangoObjectPermissions, IsOwner

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProductModelSerializer
        return super().get_serializer_class()


class ClientModelViewSet(ModelViewSet):
    queryset = User.objects.filter(type=User.Type.CLIENT)
    serializer_class = ClientModelSerializer


class MerchantModelViewSet(ModelViewSet):
    queryset = User.objects.filter(type=User.Type.MERCHANT)
    serializer_class = MerchantModelSerializer
