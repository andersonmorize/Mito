# Generated by Django 3.2.8 on 2021-10-07 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ediatado em')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('cod_hex', models.CharField(blank=True, max_length=6, null=True, verbose_name='Codigo Hexadecimal')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ediatado em')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ediatado em')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('description', models.TextField(default='Essa é top visse', verbose_name='Descrição')),
                ('size', models.CharField(choices=[('Vestimenta', (('pp', 'PP'), ('p', 'P'), ('m', 'M'), ('g', 'G'), ('gg', 'GG'))), ('Calçado', (('36', '36'), ('38', '38'), ('40', '40'), ('42', '42'), ('44', '44'), ('46', '46')))], max_length=2, verbose_name='Tamanho')),
                ('sex', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino'), ('u', 'Unissex')], max_length=15)),
                ('image', models.ImageField(upload_to='imagens/%Y/%m', verbose_name='Imagem')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ediatado em')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.color')),
                ('tags', models.ManyToManyField(to='product.Tag')),
            ],
        ),
    ]
