# Generated by Django 3.2.8 on 2021-10-07 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20211007_0330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invetory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0, verbose_name='Quantidade')),
            ],
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='product.invetory', verbose_name='Quantidade'),
            preserve_default=False,
        ),
    ]
