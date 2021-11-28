from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from tag.models import Tag
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class TagListView(LoginRequiredMixin, ListView):
    model = Tag
    template_name = 'tag/index.html'
    paginate_by = 10
    context_object_name = 'tags'



class TagCreateView(LoginRequiredMixin, CreateView):
    model = Tag
    fields = "__all__"
    template_name = 'tag/form.html'
    success_url = '/tags/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Adicionar Tag'

        return context


class TagUpdateView(LoginRequiredMixin, UpdateView):
    model = Tag
    fields = "__all__"
    template_name = 'tag/form.html'
    success_url = '/tags/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Editar Tag'

        return context

