# Generated by Django 3.2.8 on 2021-10-11 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
        ('product', '0016_auto_20211011_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='brand.brand', verbose_name='Marca'),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
    ]
