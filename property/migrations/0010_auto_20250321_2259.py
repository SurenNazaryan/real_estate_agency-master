# Generated by Django 2.2.24 on 2025-03-21 19:59

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20250321_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Нормализированный номер владельца:'),
        ),
    ]
