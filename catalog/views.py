from product.models import Product
from category.models import Category
from tag.models import Tag
from brand.models import Brand
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView

from django.db.models import Q


class CatalogListView(ListView):
    model = Product
    paginate_by = 8
    context_object_name = 'products'
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['tags'] = Tag.objects.all()
        context['title_session'] = 'Produtos'

        return context

    def get_queryset(self):
        qs = super().get_queryset()

        qs = qs.filter(status=True)

        return qs
    


class CatalogDetailView(DetailView):
    model = Product
    template_name = 'catalog/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_tags'] = Tag.objects.filter(product=self.object.id)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class CatalogCategoryListView(CatalogListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_session'] = 'Categoria: ' + self.kwargs.get('category', None)

        return context

    def get_queryset(self):
        qs = super().get_queryset()

        category = self.kwargs.get('category', None)

        if not category:
            return qs

        qs = qs.filter(category__name__iexact=category)

        return qs



class CatalogTagListView(CatalogListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_session'] = 'Tag: ' + self.kwargs.get('tag', None)

        return context

    def get_queryset(self):
        qs = super().get_queryset()

        tag = self.kwargs.get('tag', None)

        if not tag:
            return qs

        qs = qs.filter(tags__name__iexact=tag)

        return qs



class CatalogBrandListView(CatalogListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title_session'] = 'Marca: ' + self.kwargs.get('brand', None)

        return context

    def get_queryset(self):
        qs = super().get_queryset()

        brand = self.kwargs.get('brand', None)

        if not brand:
            return qs

        qs = qs.filter(brand__name__iexact=brand)

        return qs


class CatalogSearchListView(CatalogListView):

    def get_queryset(self):
        qs = super().get_queryset()
        
        search = self.request.GET.get('search')

        if not search:
            return qs

        qs = qs.filter(
            Q(name__icontains=search) |
            Q(category__name__iexact=search) |
            Q(brand__name__iexact=search) |
            Q(tags__name__iexact=search) |
            Q(description__icontains=search)
        )

        return qs


class CatalogSexListView(CatalogListView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sex = self.kwargs.get('sex', None)

        if sex == 'm':
            gender = 'Masculino'
        elif sex == 'f':
            gender = 'Feminino'
        else:
            gender = 'Unissex'
            
        context['title_session'] = 'Gênero: ' + gender

        return context
    
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        sex = self.kwargs.get('sex', None)

        if not sex:
            return qs

        qs = qs.filter(
            Q(sex__exact=sex)
        )

        return qs