from django.urls import path
from product.views import (
    # Product
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDetailView,
    ProductDeleteView,
    ProductCategoryListView,
    ProductBrandListView,
    ProductTagListView,
    ProductSearchListView,
    # Size
    ProductSizeCreateView,
    ProductSizeUpdateView,
    ProductSizeAddOneView,
    ProductSizeSubtractOneView,
    ProductSizeAddMoreView,
    ProductSizeSubtractMoreView,
)


urlpatterns = [
    # Products
    path('', ProductListView.as_view(), name='index'),
    path('create', ProductCreateView.as_view(), name='create'),
    path('<pk>/detail', ProductDetailView.as_view(), name='detail'),
    path('<pk>/update', ProductUpdateView.as_view(), name='update'),
    path('<pk>/delete', ProductDeleteView.as_view(), name='delete'),
    # Product Category
    path('category/<str:category>',
        ProductCategoryListView.as_view(), name='product_category'),
    # Product Brand
    path('brand/<str:brand>',
        ProductBrandListView.as_view(), name='product_brand'),
    # Product Tag
    path('tag/<str:tag>',
        ProductTagListView.as_view(), name='product_tag'),
    # Product Search
    path('search',
        ProductSearchListView.as_view(), name='product_search'),
    #Size
    path('<int:product>/sizes/create',
        ProductSizeCreateView.as_view(), name='product_size_create'),
    path('<int:product>/sizes/<pk>/update',
        ProductSizeUpdateView.as_view(), name='product_size_update'),
    # Add and subtract amount in Size
    path('<int:product>/sizes/<pk>/add-one',
        ProductSizeAddOneView.as_view(), name='product_size_add'),
    path('<int:product>/sizes/<pk>/subtract-one',
        ProductSizeSubtractOneView.as_view(),
        name='product_size_subtract'),
    path('<int:product>/sizes/<pk>/add-more',
        ProductSizeAddMoreView.as_view(),
        name='product_size_add_more'),
    path('<int:product>/sizes/<pk>/subtract-more',
        ProductSizeSubtractMoreView.as_view(),
        name='product_size_subtract_more')
]

