# Generated by Django 3.2.8 on 2021-12-30 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_auto_20211011_0308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.CreateModel(
            name='Sizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('Vestimenta', (('pp', 'PP'), ('p', 'P'), ('m', 'M'), ('g', 'G'), ('gg', 'GG'))), ('Calçado', (('36', '36'), ('38', '38'), ('40', '40'), ('42', '42'), ('44', '44'), ('46', '46')))], max_length=2, verbose_name='Tamanho')),
                ('amount', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='Produto ID')),
            ],
        ),
    ]
