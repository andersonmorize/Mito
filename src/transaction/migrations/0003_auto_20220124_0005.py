# Generated by Django 3.2.8 on 2022-01-24 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0025_alter_size_product'),
        ('transaction', '0002_auto_20220123_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='product',
        ),
        migrations.AddField(
            model_name='transaction',
            name='size',
            field=models.ForeignKey(null=True, default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='product.size', verbose_name='Produto'),
            preserve_default=False,
        ),
    ]
