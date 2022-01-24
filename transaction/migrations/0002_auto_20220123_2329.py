# Generated by Django 3.2.8 on 2022-01-24 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0022_alter_size_product'),
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='size',
        ),
        migrations.AddField(
            model_name='transaction',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='product.product', verbose_name='Produto'),
            preserve_default=False,
        ),
    ]
