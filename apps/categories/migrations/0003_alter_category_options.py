# Generated by Django 4.2.16 on 2024-11-06 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_alter_category_image_alter_category_imagebig'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
