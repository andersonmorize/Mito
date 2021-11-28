from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from category.models import Category
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category/index.html'
    paginate_by = 10
    context_object_name = 'categories'



class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = "__all__"
    template_name = 'category/form.html'
    success_url = '/categories/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Adicionar Categoria'

        return context


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = "__all__"
    template_name = 'category/form.html'
    success_url = '/categories/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Editar Categoria'

        return context

