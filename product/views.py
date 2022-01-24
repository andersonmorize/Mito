from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.db.models import Q

from django.views.generic.base import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)

from product.models import Product, Size
from tag.models import Tag
from category.models import Category
from brand.models import Brand
from transaction.models import Transaction

from product.forms import ProductForm, SizeForm


class ProductListView(LoginRequiredMixin, ListView):
    """View all the products"""
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
    """Create a product.
    
    If successful, redirect to the newly created product.
    """
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
    """View a specific product"""
    model = Product
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sizes'] = Size.objects.filter(
            product=self.object.id)
        context['tags'] = Tag.objects.filter(
            product=self.object.id)
        
        context['transactions'] = Transaction.objects.filter(
            size__in=self.object.size.all()[:10])
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Update a product.
    
    If successful, redirect to the newly updated product.
    """
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
    """Delete a product.
    If successful, redirect to all products."""
    model = Product
    template_name = 'product/delete.html'
    success_url = '/products/'


class ProductCategoryListView(ProductListView):
    """View all products in a category"""
    
    def get_queryset(self):
        qs = super().get_queryset()
        category = self.kwargs.get('category', None)

        if not category:
            return qs

        qs = qs.filter(category__name__iexact=category)

        return qs


class ProductBrandListView(ProductListView):
    """View all products in a brand."""
    
    def get_queryset(self):
        qs = super().get_queryset()
        brand = self.kwargs.get('brand', None)

        if not brand:
            return qs

        qs = qs.filter(brand__name__iexact=brand)

        return qs



class ProductTagListView(ProductListView):
    """View all products in a tag."""

    def get_queryset(self):
        qs = super().get_queryset()
        tag = self.kwargs.get('tag', None)

        if not tag:
            return qs

        qs = qs.filter(tags__name__iexact=tag)

        return qs


class ProductSearchListView(ProductListView):
    """View all products where the search string in contained in
    the product names."""

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search')

        if not search:
            return qs

        qs = qs.filter(Q(name__icontains=search))

        return qs

# Start of logic for Model 'Size'
class ProductSizeCreateView(LoginRequiredMixin, CreateView):
    """Create a size for a specific product.
    
    If successful, redirect to the specified product.
    """
    model = Size
    form_class = SizeForm
    template_name = 'size/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Adicionar Tamanho'
        product = Product.objects.get(id=self.kwargs.get('product'))
        context['form'] = self.form_class(initial={'product': product.id})
        return context

    def get_success_url(self):
        return f'/products/{self.object.product.id}/detail'
    
    
class ProductSizeUpdateView(LoginRequiredMixin, UpdateView):
    """Updates a specific size of a specific product.
    
    If successful, redirect to the specified product.
    """
    model = Size
    form_class = SizeForm
    template_name = 'size/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Editar Tamanho'
        product = Product.objects.get(id=self.kwargs.get('product'))
        context['form'] = SizeForm(initial={
            'product': product.id, 
            'amount': self.object.amount,
            'size': self.object.size
        })
        return context

    def get_success_url(self):
        return f'/products/{self.object.product.id}/detail'
    

class ProductSizeAddOneView(LoginRequiredMixin, View):
    """Adds a unit to a specific product and size.
    
    If successful, redirect to the specific product.
    """    
    http_method_names = ['post']
    
    def post(self, request, product, pk):
        size_ = Size.objects.get(id=pk)
        size_.amount = size_.amount + 1
        size_.save()
        
        # Create trasaction for added product
        Transaction.objects.create(
            size=size_,
            amount=1,
            unit_price=size_.product.price
        )
        
        return redirect('detail', pk=product)


class ProductSizeSubtractOneView(LoginRequiredMixin, View):
    """Subtracts a unit from a specific product and size.
    
    If successful, redirect to the specific product.
    """
    http_method_names = ['post']
    
    def post(self, request, product, pk, *args, **kwargs):
        size_ = Size.objects.get(id=pk)
        
        if size_.amount - 1 >= 0:    
            size_.amount = size_.amount - 1
            size_.save()
            
        # Create trasaction for added product
        Transaction.objects.create(
            size=size_,
            amount=-1,
            unit_price=size_.product.price
        )
        
        return redirect('detail', pk=product)
    

class ProductSizeAddMoreView(LoginRequiredMixin, UpdateView):
    """Add units to a specify size."""
    model = Size
    form_class = SizeForm
    template_name = 'size/form-add-more.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Adicionar quantidade'
        # Used to block size choice
        context['update'] = True
        size = self.model.objects.get(id=self.kwargs.get('pk'))
        context['form'] = self.form_class(initial={
            'product': size.product.id, 
            'amount': 0,
            'size': size.size
        })
        return context

    def post(self, request, **kwargs):
        add_amount = int(request.POST.get('amount'))        
        size = Size.objects.get(id=kwargs.get('pk'))
        size.amount += add_amount
        size.save()
        return redirect('detail', pk=size.product.id)


class ProductSizeSubtractMoreView(ProductSizeAddMoreView):
    """Subtract units to a specify size."""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_page'] = 'Remover quantidade'
        # Used to block size choice
        context['update'] = True
        return context
    
    def post(self, request, *args, **kwargs):
        subtract_amount = int(request.POST.get('amount'))        
        size = Size.objects.get(id=kwargs.get('pk'))
        
        if size.amount - subtract_amount >= 0:
            size.amount -= subtract_amount 
            size.save()
        
        return redirect('detail', pk=size.product.id)
