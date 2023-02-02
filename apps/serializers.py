from rest_framework.fields import HiddenField, CurrentUserDefault, SerializerMethodField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Category, Product, User


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id',)


class CreateProductModelSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('id',)


class ClientModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class MerchantModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'date_joined')


class ProductModelSerializer(ModelSerializer):
    owner = SerializerMethodField('get_owner')

    def get_owner(self, obj):
        return obj.owner.username

    class Meta:
        model = Product
        fields = '__all__'
