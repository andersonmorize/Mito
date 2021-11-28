# Generated by Django 3.2.8 on 2021-10-07 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.color', verbose_name='Cor'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sex',
            field=models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino'), ('u', 'Unissex')], max_length=15, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='product.Tag', verbose_name='Tags'),
        ),
    ]
