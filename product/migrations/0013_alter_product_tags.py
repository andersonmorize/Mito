# Generated by Django 3.2.8 on 2021-10-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20211009_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(db_constraint=False, to='product.Tag', verbose_name='Tags'),
        ),
    ]
