# Generated by Django 4.1.6 on 2023-02-02 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_product_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('see_premium_product', 'Can see premium products')]},
        ),
    ]
