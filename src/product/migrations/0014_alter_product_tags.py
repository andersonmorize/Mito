# Generated by Django 3.2.8 on 2021-10-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='product.Tag', verbose_name='Tags'),
        ),
    ]
