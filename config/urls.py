from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', include('catalog.urls')),
    path('products', include('product.urls')),
    path('transactions', include('transaction.urls')),
    path('categories', include('category.urls')),
    path('tags', include('tag.urls')),
    path('brands', include('brand.urls')),
    path('dashboard', include('dashboard.urls')),
    path('chupameucu', include('django.contrib.auth.urls')),
    path('summernote', include('django_summernote.urls')),
    path('admin', admin.site.urls),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
