# Generated by Django 3.2.8 on 2021-10-07 08:05

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('product', '0006_rename_amount_product_invetory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Invetory',
            new_name='Inventory',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='invetory',
            new_name='inventory',
        ),
    ]
