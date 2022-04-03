# Generated by Django 3.2.8 on 2021-10-11 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('product', '0014_alter_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='category.category', verbose_name='Categoria'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]