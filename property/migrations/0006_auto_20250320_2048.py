# Generated by Django 2.2.24 on 2025-03-20 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20250319_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.Flat', verbose_name='Квартира, на которую пожаловались:'),
        ),
    ]
