from django.db import models



class Brand(models.Model):
    
    class Meta:
        ordering = ['name']


    name = models.CharField(max_length=100, verbose_name='Nome')

    created_at = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Ediatado em', auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'

