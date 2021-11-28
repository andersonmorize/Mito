from django.forms import ModelForm
from output.models import Output
from django import forms



class OutputForm(ModelForm):

    class Meta:
        model = Output
        fields = ('product', 'amount', 'price', ) 

