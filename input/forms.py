from django.forms import ModelForm
from input.models import Input


class InputForm(ModelForm):        

    class Meta:
        model = Input
        fields = ('product', 'amount', 'price', ) 

