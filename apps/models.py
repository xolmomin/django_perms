from django.contrib.auth.models import AbstractUser
from django.db import models

'''
merchant, client, manager, staff tipli userlar boladi

comment product ga tegishli boladi (commentni egasi add, change qiladi, manager delete qiladi oladi)

task managar tomonidan stafflarga beriladi (staff change qiladi oladi[status], manager delete, add, change)

'''
# IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly


class User(AbstractUser):
    class Type(models.TextChoices):
        MERCHANT = 'merchant', 'Sotuvchi'
        CLIENT = 'client', 'Haridor'

    type = models.CharField(max_length=25, choices=Type.choices, default=Type.CLIENT)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('apps.Category', models.CASCADE)
    is_premium = models.BooleanField(default=False)
    owner = models.ForeignKey('apps.User', models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        permissions = [
            ('see_premium_product', 'Can see premium products')
        ]
