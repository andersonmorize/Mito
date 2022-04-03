from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from brand.models import Brand
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class BrandListView(LoginRequiredMixin, ListView):
    model = Brand
    template_name = 'brand/index.html'
    paginate_by = 10
    context_object_name = 'brands'



class BrandCreateView(LoginRequiredMixin, CreateView):
    model = Brand
    fields = "__all__"
    template_name = 'brand/form.html'
    success_url = '/brands/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Adicionar Marca'

        return context


class BrandUpdateView(LoginRequiredMixin, UpdateView):
    model = Brand
    fields = "__all__"
    template_name = 'brand/form.html'
    success_url = '/brands/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Editar Marca'

        return context


