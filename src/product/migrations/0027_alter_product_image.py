# Generated by Django 3.2.8 on 2022-03-25 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20220124_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m', verbose_name='Imagem'),
        ),
    ]
