# Generated by Django 4.0.1 on 2022-01-23 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_name',
            new_name='product_name',
        ),
    ]
