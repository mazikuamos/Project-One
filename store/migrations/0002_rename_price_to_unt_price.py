# Generated by Django 4.1.5 on 2023-01-17 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='unt_price',
        ),
    ]