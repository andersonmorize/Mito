from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.CatalogListView.as_view(), name='catalog_index'),
    path('catalog/<pk>/detail', views.CatalogDetailView.as_view(), name="catalog_detail"),
    path('category/<str:category>', views.CatalogCategoryListView.as_view(), name='catalog_category'),
    path('catalog/brand/<str:brand>', views.CatalogBrandListView.as_view(), name='catalog_brand'),
    path('tag/<str:tag>', views.CatalogTagListView.as_view(), name='catalog_tag'),
    path('search', views.CatalogSearchListView.as_view(), name='catalog_search'),
    path('sex/<str:sex>', views.CatalogSexListView.as_view(), name='catalog_sex'),
]