# Generated by Django 5.1 on 2024-08-31 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.CharField(max_length=10),
        ),
    ]
