from django.db import models
from category.models import Category
from tag.models import Tag
from brand.models import Brand


class Product(models.Model):
    CLOTHES = 1 
    SHOES = 2 
    ACCESSIRIES = 3
    
    TYPE_CHOICES = [
        (CLOTHES, 'Roupas'),
        (SHOES, 'Calçados'),
        (ACCESSIRIES, 'Acessórios'),
    ]
    
    MALE = 1
    FAMALE = 2
    UNISEX = 3

    SEX_CHOICES = [
        (MALE, 'Masculino'),
        (FAMALE, 'Feminino'),
        (UNISEX, 'Unissex')
    ]

    name = models.CharField(
        max_length=255, verbose_name='Nome')
    description = models.TextField(
        default='Essa é top visse', verbose_name='Descrição')
    price = models.FloatField(
        default=0, verbose_name='Preço')
    color = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Cor')
    sex = models.PositiveSmallIntegerField(
        choices=SEX_CHOICES, verbose_name='Sexo')
    type_product = models.PositiveSmallIntegerField(
        choices=TYPE_CHOICES, verbose_name='Tipo')
    image = models.ImageField(
        upload_to='images/%Y/%m', verbose_name='Imagem')
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, verbose_name='Categoria')
    brand = models.ForeignKey(
        Brand, on_delete=models.DO_NOTHING, verbose_name='Marca')
    tags = models.ManyToManyField(
        Tag, verbose_name='Tags')
    status = models.BooleanField(
        default=False)
    created_at = models.DateTimeField(
        verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Ediatado em', auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self) -> str:
        return f'#{self.id} - {self.name}'
    

class Size(models.Model):
    
    SIZE_CHOICES = [
        ('Vestimenta', (
                ('pp', 'PP'), 
                ('p', 'P'),
                ('m', 'M'),
                ('g', 'G'),
                ('gg', 'GG')
            )
        ),
        ('Calçado', (
                ('36', '36'),
                ('38', '38'),
                ('40', '40'),
                ('42', '42'),
                ('44', '44'),
                ('46', '46')
            )
        )
    ]
    
    size = models.CharField(
        max_length=2, choices=SIZE_CHOICES, verbose_name='Tamanho')
    amount = models.IntegerField(
        default=0, verbose_name='Quantidade')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, verbose_name='Produto',
        related_name='size')

    class Meta:
        unique_together = ('size', 'product',)    
    
    def __str__(self):
        print(dir(self.size))
        return f'{self.size.upper()}'
        




