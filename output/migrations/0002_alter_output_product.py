# Generated by Django 3.2.8 on 2021-10-09 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_alter_product_tags'),
        ('output', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='output',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Produto'),
        ),
    ]
