from rest_framework.decorators import action
from rest_framework.permissions import DjangoObjectPermissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.models import Category, Product, User
from apps.permissions import IsOwner, CustomDjangoObjectPermissions, IsPremiumUser, IsAdminUserOrReadOnly
from apps.serializers import CategoryModelSerializer, ProductModelSerializer, ClientModelSerializer, \
    MerchantModelSerializer, CreateProductModelSerializer, UserModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, \
    AllowAny, NOT, AND, OR, \
    DjangoModelPermissions, DjangoObjectPermissions, DjangoModelPermissionsOrAnonReadOnly


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.filter(is_premium=False)
    serializer_class = ProductModelSerializer
    # permission_classes = (IsOwner & DjangoModelPermissions, )
    # permission_classes = (IsAuthenticated & IsAdminUserOrReadOnly, )
    # permission_classes = (IsAdminUserOrReadOnly & IsAuthenticated,)
    permission_classes = DjangoModelPermissions,

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProductModelSerializer
        return super().get_serializer_class()

    @action(['GET'], detail=False, url_path='premium', permission_classes=(CustomDjangoObjectPermissions,))
    def get_premium(self, request, pk=None):
        queryset = Product.objects.filter(is_premium=True)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ClientModelViewSet(ModelViewSet):
    queryset = User.objects.filter(type=User.Type.CLIENT)
    serializer_class = ClientModelSerializer


class MerchantModelViewSet(ModelViewSet):
    queryset = User.objects.filter(type=User.Type.MERCHANT)
    serializer_class = MerchantModelSerializer
