# Generated by Django 5.1 on 2024-09-01 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_order_phone_alter_order_pincode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default='', max_length=100),
        ),
    ]
