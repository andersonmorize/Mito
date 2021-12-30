from django.forms import ModelForm
from product.models import Product, Size

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'description': SummernoteWidget(),
        }
        
class SizeForm(ModelForm):
    class Meta:
        model = Size
        fields = "__all__"
        