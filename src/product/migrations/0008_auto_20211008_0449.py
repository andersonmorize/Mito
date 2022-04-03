# Generated by Django 3.2.8 on 2021-10-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20211007_0505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='inventory',
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Cor'),
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]