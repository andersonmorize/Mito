# Generated by Django 3.2.8 on 2022-01-24 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_alter_size_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='product', to='product.product', verbose_name='Produto'),
        ),
    ]
