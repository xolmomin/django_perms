# Generated by Django 4.1.6 on 2023-02-02 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_product_is_premium'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('is_premium', 'Can see premium products')]},
        ),
    ]