from django.shortcuts import render
from input.models import Input
from product.models import Product
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from input.forms import InputForm
from django.contrib.auth.mixins import LoginRequiredMixin


class InputListView(LoginRequiredMixin, ListView):
    model = Input
    template_name = 'input/index.html'
    paginate_by = 20
    context_object_name = 'inputs'

class InputCreateView(LoginRequiredMixin, CreateView):
    model = Input
    fields = "__all__"
    template_name = 'input/form.html'
    success_url = '/inputs/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Adicionar Entrada'
        product = Product.objects.get(id=self.kwargs.get('pk'))
        context['form'] = InputForm(initial={'product': product.id})

        return context


class InputProductListView(InputListView):
    
    def get_queryset(self):
        qs = super().get_queryset()

        product = self.kwargs.get('product', None)

        if not product:
            return qs

        qs = qs.filter(product=product)

        return qs



