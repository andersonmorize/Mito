from django.forms import ModelForm
from product.models import Product

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'description': SummernoteWidget(),
        }