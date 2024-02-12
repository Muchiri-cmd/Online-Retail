# Generated by Django 5.0.1 on 2024-02-12 11:35

import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_retailer_image_alter_retailer_storefront_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.user_dir_path),
        ),
        migrations.AlterField(
            model_name='retailer',
            name='storefront_image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.user_dir_path),
        ),
    ]
