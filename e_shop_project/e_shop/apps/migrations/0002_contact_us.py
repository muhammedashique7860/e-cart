# Generated by Django 5.1 on 2024-08-31 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=124)),
                ('message', models.TextField()),
            ],
        ),
    ]