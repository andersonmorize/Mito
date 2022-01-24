from django.forms import ModelForm
from transaction.models import Transaction


class TransactionForm(ModelForm):

    class Meta:
        model = Transaction
        fields = ('size', 'amount', 'unit_price', ) 

