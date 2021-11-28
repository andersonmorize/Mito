from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from product.models import Product
from tag.models import Tag
from category.models import Category
from brand.models import Brand
from input.models import Input
from output.models import Output

from product.forms import ProductForm


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product/index.html'
    paginate_by = 6
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['tags'] = Tag.objects.all()
        context['brands'] = Brand.objects.all()

        return context



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Adicionar Produto'

        return context

    def get_success_url(self):
        return f'/products/{self.object.id}/detail'


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.filter(product=self.object.id)
        context['inputs'] = Input.objects.filter(product=self.object.id)[0:5]
        context['outputs'] = Output.objects.filter(product=self.object.id)[0:5]
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    template_name = 'product/form.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Editar Produto'

        return context

    def get_success_url(self):
        return f'/products/{self.object.id}/detail'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = '/products/'


class ProductCategoryListView(ProductListView):

    def get_queryset(self):
        qs = super().get_queryset()

        category = self.kwargs.get('category', None)

        if not category:
            return qs

        qs = qs.filter(category__name__iexact=category)

        return qs


class ProductBrandListView(ProductListView):
    
    def get_queryset(self):
        qs = super().get_queryset()

        brand = self.kwargs.get('brand', None)

        if not brand:
            return qs

        qs = qs.filter(brand__name__iexact=brand)

        return qs



class ProductTagListView(ProductListView):

    def get_queryset(self):
        qs = super().get_queryset()

        tag = self.kwargs.get('tag', None)

        if not tag:
            return qs

        qs = qs.filter(tags__name__iexact=tag)

        return qs


class ProductSearchListView(ProductListView):

    def get_queryset(self):
        qs = super().get_queryset()
        
        search = self.request.GET.get('search')

        if not search:
            return qs

        qs = qs.filter(
            Q(name__icontains=search)
        )

        return qs



