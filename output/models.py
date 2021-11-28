from django.db import models
from product.models import Product


class Output(models.Model):

    class Meta:
        ordering = ['-id']

    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, blank=True, null=True, db_constraint=False, verbose_name='Produto')
    amount = models.IntegerField(verbose_name="Quantidade")
    price = models.FloatField(null=True, blank=True, verbose_name="Preço")

    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Ediatado em', auto_now=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.product:

            self.product.amount -= self.amount

            if self.product.amount >= 0:
                self.product.save()


    def __str__(self) -> str:
        return f'{self.id} - {self.amount}'

