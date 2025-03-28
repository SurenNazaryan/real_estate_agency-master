# Generated by Django 2.2.24 on 2025-03-22 10:30

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20250322_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='full_name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца:'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='normalized_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region=None, verbose_name='Нормализированный номер владельца:'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phone_number',
            field=models.CharField(db_index=True, max_length=20, verbose_name='Номер владельца:'),
        ),
    ]
