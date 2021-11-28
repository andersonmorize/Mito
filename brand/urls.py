from django.urls import path
from brand.views import (
    BrandListView,
    BrandCreateView,
    BrandUpdateView,
)


urlpatterns = [
    path('', BrandListView.as_view(), name='index_brand'),
    path('create/', BrandCreateView.as_view(), name='create_brand'),
    path('<pk>/update/', BrandUpdateView.as_view(), name='update_brand')
]