from django.shortcuts import render
from output.models import Output
from product.models import Product
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from output.forms import OutputForm
from django.contrib.auth.mixins import LoginRequiredMixin



class OutputListView(LoginRequiredMixin, ListView):
    model = Output
    template_name = 'output/index.html'
    paginate_by = 20
    context_object_name = 'outputs'

class OutputCreateView(LoginRequiredMixin, CreateView):
    model = Output
    fields = "__all__"
    template_name = 'output/form.html'
    success_url = '/outputs/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Adicionar Saída'
        product = Product.objects.get(id=self.kwargs.get('pk'))
        context['form'] = OutputForm(initial={'product': product.id, 'price': product.price})

        return context


class OutputProductListView(OutputListView):
    
    def get_queryset(self):
        qs = super().get_queryset()

        product = self.kwargs.get('product', None)

        if not product:
            return qs

        qs = qs.filter(product=product)

        return qs



