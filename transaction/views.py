from django.shortcuts import render
from transaction.models import Transaction
from product.models import Size
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from transaction.forms import TransactionForm
from django.contrib.auth.mixins import LoginRequiredMixin


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transaction/index.html'
    paginate_by = 20
    context_object_name = 'transactions'


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = "__all__"
    form_class = TransactionForm
    template_name = 'transactions/form.html'
    success_url = '/transactions/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Adicionar Entrada'
        size = Size.objects.get(id=self.kwargs.get('pk'))
        context['form'] = self.form_class(initial={'size': size.id})

        return context

