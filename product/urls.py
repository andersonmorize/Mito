from django.urls import path
from output.views import OutputCreateView
from input.views import InputCreateView
from product.views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDetailView,
    ProductDeleteView,
    ProductCategoryListView,
    ProductBrandListView,
    ProductTagListView,
    ProductSearchListView,
)


urlpatterns = [
    # Products
    path('', ProductListView.as_view(), name='index'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<pk>/detail/', ProductDetailView.as_view(), name='detail'),
    path('<pk>/update/', ProductUpdateView.as_view(), name='update'),
    path('<pk>/delete/', ProductDeleteView.as_view(), name='delete'),

    # Input / Output
    path('<pk>/add/', InputCreateView.as_view(), name='add'),
    path('<pk>/remove/', OutputCreateView.as_view(), name='remove'),

    # Product Category
    path('category/<str:category>', ProductCategoryListView.as_view(), name='product_category'),

    # Product Brand
    path('brand/<str:brand>', ProductBrandListView.as_view(), name='product_brand'),

    # Product Tag
    path('tag/<str:tag>', ProductTagListView.as_view(), name='product_tag'),

    # Product Search
    path('search/', ProductSearchListView.as_view(), name='product_search'),

]