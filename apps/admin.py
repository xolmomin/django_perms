from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from apps.models import Product, Category, User

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Permission)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
