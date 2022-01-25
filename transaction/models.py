from django.db import models
from product.models import Size

class Transaction(models.Model):
    """Used to map the inputs and outputs of products
    """
    size = models.ForeignKey(
        Size, on_delete=models.DO_NOTHING,
        null=True,
        verbose_name='Tamanho')
    amount = models.SmallIntegerField()
    unit_price = models.DecimalField(
        max_digits=6, decimal_places=2,
        verbose_name='Preço da unidade')
    created_at = models.DateTimeField(
        verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Editado em', auto_now=True)


    class Meta:
        ordering = ['-id']


    def __str__(self):
        return f'{self.id} - {self.created_at}'
    
    @property
    def product(self):
        return self.size.product.id
        
    
