from django.contrib import admin
from product.models import Product, Size

from django_summernote.admin import SummernoteModelAdmin


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Size)


