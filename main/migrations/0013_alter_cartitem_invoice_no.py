# Generated by Django 5.0.1 on 2024-03-25 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_cart_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='invoice_no',
            field=models.CharField(max_length=200, null=True),
        ),
    ]