# Generated by Django 4.2.16 on 2024-11-06 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category_images/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='imageBig',
            field=models.ImageField(upload_to='category_images/'),
        ),
    ]
