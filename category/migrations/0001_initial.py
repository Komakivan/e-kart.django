# Generated by Django 4.0.1 on 2022-01-23 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=100, unique=True)),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(blank=True)),
                ('cat_image', models.ImageField(blank=True, upload_to='photos/categories')),
            ],
        ),
    ]