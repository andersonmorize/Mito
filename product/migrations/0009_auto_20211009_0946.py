# Generated by Django 3.2.8 on 2021-10-09 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20211008_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='product.brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='product.category', verbose_name='Categoria'),
        ),
    ]
